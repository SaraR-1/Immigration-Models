import pandas as pd
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from collections import defaultdict

def panel_regression(y, xs, years, country, list_x, save = True, path = ""):
    data = bdf.filter_origin_country_dataset(y, country, years, xs.index.levels[0].tolist(), xs)

    mod = PanelOLS(data.y, data[list_x])
    res = mod.fit()
    print("The R-squared of the regression model using the independent variables %s is %f." %(list_x, res.rsquared))

    plot_real_VS_prediction(y, xs, years, country, rot, "Regression model using the independent var %s" %list_x, save, path)


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
