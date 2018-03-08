import pandas as pd
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from collections import defaultdict
import build_data_functions as bdf
from linearmodels.panel  import PanelOLS, FirstDifferenceOLS
import plot_model_functions as pmf
import statsmodels.api as sm

def panel_regression(y, xs, years, country, list_x, prev = 0, save = True, path = "", diff = False, constant = False):
    data = bdf.filter_origin_country_dataset(y, country, years, xs.index.levels[0].tolist(), xs, prev)
    if constant == False:
        exog = data[list_x]
    else:
        exog = sm.add_constant(data[list_x])
    #
    if diff == False:
            mod = PanelOLS(data.y, exog)
    else:
        mod = FirstDifferenceOLS(data.y, exog)
    res = mod.fit()
    print("The R-squared of the regression model is %f." %res.rsquared)
    print("Estimated parameters:")
    print(pd.DataFrame(res.params))

    R2 = 1 - sum(np.subtract((data["y"]).values, res.fitted_values.fitted_values.values)**2) / sum(((data["y"]).values - np.mean((data["y"]).values))**2)
    # k: number of independet vars
    k = 1
    n = len(data["y"].values)
    R2_adj = 1 - (1 - R2)*((n - 1)/(n - k -1))
    print("My R2: %f, adj-R2: %f." %(R2, R2_adj))

    pmf.plot_real_VS_prediction(y, res.fitted_values, xs, years, country, 45, "Regression model", save, path)

    return(res.params, res.fitted_values)


# Get the foreigners stock value
def n_it(data_, i, t):
    return(data_[(data_["Province"] == i) & (data_["Year"] == t)]["Value"].values[0])

def count(data_):
    count_obj = defaultdict(lambda: 0)
    for i in data_:
        count_obj[i] += 1
    return(count_obj)

# Do not consider provinces with missing values (0 immigrants) for more than two years (>= 3) (My Assumption!)
def not_including(data_, times, territories):
    temp_not_in = list()
    for i in territories:
        for t in times:
            try:
                temp = data_[(data_["Province"] == i) & (data_["Year"] == t)]["Value"].values[0]
            except IndexError:
                temp_not_in.append(i)
    not_in_count = count(temp_not_in)
    not_in = [k for k, v in not_in_count.items() if v >= 3]
    return(not_in)
