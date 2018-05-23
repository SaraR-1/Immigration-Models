#%%
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

import numpy as np
import os
import sys
sys.path.append('/home/sara/Documents/Immigration/Shared_models')
from statsmodels.datasets import grunfeld
from linearmodels.panel import PanelOLS
import pandas as pd
import build_data_functions as bdf
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import model_functions as mf
import plot_model_functions as pmf
import panelOLS_models
import statsmodels.api as sm
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression


#%%
# We can start from 2003 because we 2002 is the first available additional data
years = list(range(2003, 2017))
y = pd.read_table(
    "/home/sara/Documents/Immigration/Shared_models/Spain/Data/spain_working_aut_comm.tsv", sep="\t", index_col=0)
y = y.groupby(["Province", "Country", "Year"], as_index=False)["Value"].sum()
y = bdf.pivot(y, "Country", "Value")

xs = pd.read_table("Data/xs_aut_comm.tsv", sep="\t",
                   index_col=["Province", "Year"])
xs = xs.shift()
xs = xs.loc[(slice(None), years), ]

palette = ['blue', 'darkgreen', 'yellowgreen', 'orange', 'lightcoral',
           'red', 'paleturquoise', 'deepskyblue', 'mediumpurple', 'fuchsia']

#%%
directory = "/home/sara/Documents/Immigration/Shared_models/Spain/Regression_%d_%d" % (
    years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)

countries_list = ['Ecuador', 'Germany', 'Morocco', 'Peru', 'Poland', 'Romania']

#%%
for country in countries_list:
    print("------------------------------- %s -------------------------------" % country)
    panelOLS_models.panel_regression(y, xs, years, country, [
        3, 5, 7, 9, 11], list(xs.index.levels[0]), palette, "Regression Model %s" % country, directory, manual_sel=False, title_add=" in Spanish Autonomous Communities")

