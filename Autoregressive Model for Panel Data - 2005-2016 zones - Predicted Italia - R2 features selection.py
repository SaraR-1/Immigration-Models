#%%
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")
    
import numpy as np
from statsmodels.datasets import grunfeld
from linearmodels.panel  import PanelOLS
import pandas as pd
import build_data_functions as bdf
import plot_data_functions as pdf
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import model_functions as mf
import plot_model_functions as pmf
import panelOLS_models 
import spatial_error_model as sem
import spatial_error_model_new as semnew
import statsmodels.api as sm
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression
import pycountry
import os
from sys import argv
import json
from collections import defaultdict
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.preprocessing import normalize

from sklearn.model_selection import train_test_split, ShuffleSplit, cross_val_score
from scipy.stats import normaltest

#%%
years = list(range(2005, 2017))
directory = "/home/sara/Documents/Immigration/Shared_models/Paper_%d_%d" % (
    years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)
    
#%%
y = pd.read_table(
    "/home/sara/Documents/Immigration/Shared_models/Data/resident_foreigners_norm.csv", sep="\t", index_col=0)
y = y.groupby(["Province", "Country", "Year"], as_index=False)["Value"].sum()
y = bdf.pivot(y, "Country", "Value")

resident_foreigners_norm = pd.read_table(
    "/home/sara/Documents/Immigration/Shared_statistics/Data_final/resident_foreigners_norm.csv")

#%%
# To get the Italy info we need to sum the 5 Italian zones
zones = list(pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/x_zones.csv",
                           sep="\t", index_col=["Province", "Year"]).index.levels[0])

for t in y.index.levels[1]:
    y.loc[("Italia", t), :] = y.loc[(zones, t), :].sum()
temp = pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/x_zones.csv",
                     sep="\t", index_col=["Province", "Year"])
xs = pd.DataFrame(columns=["Province", "Year"]+temp.columns.tolist())
xs = xs.set_index(["Province", "Year"])

for t in temp.index.levels[1]:
    xs.loc[("Italia", t), :] = temp.loc[(zones, t), :].sum()

palette = ['blue', 'darkgreen', 'yellowgreen', 'orange', 'lightcoral',
           'red', 'paleturquoise', 'deepskyblue', 'mediumpurple', 'fuchsia']

'''countries_list = ["Romania", "Morocco", "Albania", "Tunisia",
                  "Egypt", "Ecuador", "Peru", "China", "Philippines"]'''

countries_list = ['China', 'Colombia', 'Ecuador', 'Germany', 'Morocco', 'Romania']

countries_list_iso3 = [pycountry.countries.get(
    name=country).alpha_3 for country in countries_list]
target = "Italia"
# number of features to select
ks = [3, 5, 7, 10, 15]

y_hat, models = mf.compute_regression_model(
    y, xs, years, countries_list, target, ks)

y_hat.to_csv(directory+"/predicted_italia.tsv", sep="\t")

'''pdf.relation_plot_time_variant_intern_function(y_hat, countries_list_iso3, years, ["Predicted"], resident_foreigners_norm.groupby(["Country", "Year"]), plt.figure(
    1, figsize=(15, 14)), 331, 45, palette, None, "Immigrant Stock Real VS Predicted", True, directory+"/regression_model_italy", False)
'''

pdf.relation_plot_time_variant_intern_function(y_hat, countries_list_iso3, years, ["Predicted"], resident_foreigners_norm.groupby(["Country", "Year"]), plt.figure(
    1, figsize=(15, 14)), 231, 45, palette, None, "Immigrant Stock Real VS Predicted in Italy", True, directory+"/regression_model_italy", False)


y_italia_pred = y.copy()
for country in countries_list_iso3:
    y_italia_pred.loc[("Italia", years), country] = np.array(
        y_hat.loc[(slice(None), country), "Predicted"].values, dtype=np.float32)
        
for k1 in models.keys():
    models[k1]["coefficients"] = list(models[k1]["coefficients"])

res_it = defaultdict(dict)

for k1 in models.keys():
    for k2, v in zip(models[k1]["features"], models[k1]["coefficients"]):
        res_it[k1][k2] = v

with open(directory+"/regression_model_italy.txt", 'w') as outfile:
    json.dump(res_it, outfile)

#%%
xs_zones = pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/x_zones.csv",
                         sep="\t", index_col=["Province", "Year"])
xs_zones = pd.concat([xs_zones, xs])
zones_data = pd.read_table(
    "/home/sara/Documents/Immigration/Shared_statistics/Data_final/territori.csv")
zones_data = zones_data.replace(
    ['Provincia Autonoma Bolzano / Bozen', 'Provincia Autonoma Trento'], ['Bolzano / Bozen', 'Trento'])
# Distance matrix related to the interested locations (regions capitals)
temp_W = pd.read_table(
    "/home/sara/Documents/Immigration/Shared_models/Data/Zones_distances_matrix_mean.csv", sep="\t", index_col=0)

# Add Italy distance info as mean of the five zones
temp_W["Italia"] = [temp_W.loc[z].mean() for z in temp_W.index]
temp_W.loc["Italia"] = [temp_W.loc[z].mean() for z in temp_W.index] + [0]
temp_W = (1/temp_W)**2
# w_ij = 0 if i=j
temp_W[temp_W == np.inf] = 0
# row standardization: every arow sum up to 1
temp_W = temp_W.div(temp_W.sum(axis=1), axis=0)
# Just to make sure the matrix has the right sort
temp_W = temp_W.sort_index(axis=1)
temp_W = temp_W.sort_index(axis=0)
#palette = sns.color_palette()
palette = ['blue', 'darkgreen', 'yellowgreen', 'orange', 'lightcoral',
           'red', 'paleturquoise', 'deepskyblue', 'mediumpurple', 'fuchsia']

#%% 
for c in countries_list:
    print("------------------------------- %s -------------------------------" % c)
    test_size = 3
    res_pred, res_est, res_params = semnew.run_model(y, c, years, "Italia", xs_zones, temp_W, temp_W.columns.tolist(
    ), False, palette, "Spatial Error Model", save=True, path=directory+"/spatial_autocorr_model_%s_" % c.lower(), data_hat=y_italia_pred, train_test=True, test_size=test_size)
    res_pred.to_csv(
        directory+"/spatial_autocorr_model_fitted_values_%s.tsv" % c.lower(), sep='\t')
    res_est.to_csv(
        directory+"/spatial_autocorr_model_est_params2_%s.tsv" % c.lower(), sep='\t')
    res_params.to_csv(
        directory+"/spatial_autocorr_model_est_params1_%s.tsv" % c.lower(), sep='\t')

