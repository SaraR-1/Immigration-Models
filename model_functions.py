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
from sklearn.metrics import r2_score

def panel_regression(y, xs, years, country, list_x, prev = 0, show = False, save = True, path = "", diff = False, constant = False, entity_effects = False):
    data = bdf.filter_origin_country_dataset(y, country, years, xs.index.levels[0].tolist(), xs, prev)
    if constant == False:
        exog = data[list_x]
    else:
        exog = sm.add_constant(data[list_x])
    #
    if diff == False:
            mod = PanelOLS(data.y, exog, entity_effects = entity_effects)
    else:
        mod = FirstDifferenceOLS(data.y, exog)
    res = mod.fit()
    #print("The R-squared of the regression model is %f." %res.rsquared)
    #print("Estimated parameters:")
    #print(pd.DataFrame(res.params))

    evaluation(data, res.fitted_values, constant, len(xs.columns.tolist()))

    if show == True:
            pmf.plot_real_VS_prediction(y, res.fitted_values, xs, years, country, 45, "Regression model", save, path)
    else:
        pass

    return(res.params, res.fitted_values)


def panel_regression_training_test(y, xs, years_training, years_test, country, list_x, prev = 0, show = False, save = True, path = "", diff = False, constant = False, entity_effects = False):
    years = years_training + years_test
    data = bdf.filter_origin_country_dataset(y, country, years, xs.index.levels[0].tolist(), xs, prev)

    data_tr = data.loc[(slice(None), years_training), :]
    data_te = data.loc[(slice(None), years_test), :]

    if constant == False:
        exog_tr = data_tr[list_x]
        exog_te = data_te[list_x]
    else:
        exog_tr = sm.add_constant(data_tr[list_x])
        exog_te = sm.add_constant(data_te[list_x])
    #
    if diff == False:
            mod = PanelOLS(data_tr.y, exog_tr, entity_effects = entity_effects)
    else:
        mod = FirstDifferenceOLS(data_tr.y, exog_tr)
    res_tr = mod.fit()

    #print("---------------- Training Results ----------------")
    #evaluation(data_tr, res_tr.fitted_values, constant)

    fitted_values_te = res_tr.params.values*exog_te
    fitted_values_te["fitted_values"] = fitted_values_te.sum(axis=1)
    fitted_values_ = fitted_values_te.append(res_tr.fitted_values)
    fitted_values_ = fitted_values_.sort_index()
    if show == True:
        pmf.plot_real_VS_prediction(y, fitted_values_, xs, years, country, 45, "Regression model", save = save, path = "")
    else:
        pass

    print("-------------- Trainin-Test  Results --------------")
    evaluation(data, fitted_values_, constant, len(xs.columns.tolist()))

    return(res_tr.params, fitted_values_)

def evaluation(data, y_hat, constant, k):
    if constant == False:
        R2 = 1 - (sum(np.subtract(data["y"].values, y_hat.fitted_values.values)**2) / sum((data["y"].values)**2))
    else:
        R2 = 1 - (sum(np.subtract(data["y"].values, y_hat.fitted_values.values)**2) / sum((data["y"].values - np.mean(data["y"].values))**2))

    print("R-squared %f." %round(R2,3))
    # k: number of independet vars
    n = len(data["y"].values)
    R2_adj = 1 - (1 - R2)*((n - 1)/(n - k -1))
    print("Adjusted R-squared %f." %round(R2_adj, 3))

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
