#%%
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")
    
import numpy as np
import os
from statsmodels.datasets import grunfeld
from linearmodels.panel  import PanelOLS
import pandas as pd
import sys
sys.path.append('/home/sara/Documents/Immigration/Shared_models')
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
# From 2006 because we are using the independent regressors at time t-1. Those data are available form 2005, used for the prediction of 2006
years = list(range(2006, 2017))
y = pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/resident_foreigners_norm.csv", sep = "\t", index_col=0)
y = y.groupby(["Province", "Country", "Year"], as_index=False)["Value"].sum()
y = bdf.pivot(y, "Country", "Value")


xs = pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/x_zones.csv",
                   sep="\t", index_col=["Province", "Year"])

xs = xs.shift()
xs = xs.loc[(slice(None), years), ]

zones_data = pd.read_table(
    "/home/sara/Documents/Immigration/Shared_statistics/Data_final/territori.csv")
zones_data = zones_data.replace(
    ['Provincia Autonoma Bolzano / Bozen', 'Provincia Autonoma Trento'], ['Bolzano / Bozen', 'Trento'])

palette = ['blue', 'darkgreen', 'yellowgreen', 'orange', 'lightcoral',
               'red', 'paleturquoise', 'deepskyblue', 'mediumpurple', 'fuchsia']

#%%
directory = "/home/sara/Documents/Immigration/Shared_models/Regression_%d_%d" % (
    years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)

countries_list = ['Germany', 'Morocco', 'Peru', 'Poland', 'Romania']

for country in countries_list:
    print("------------------------------- %s -------------------------------" % country)
    panelOLS_models.panel_regression(y, xs, years, country, [
        3, 5, 7, 10, 15], zones_data, palette, "Regression Model %s" % country, directory)

