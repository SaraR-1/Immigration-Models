#%%
import pandas as pd
import numpy as np
import sys
sys.path.append('/home/sara/Documents/Immigration/Shared_models')
import build_data_functions as bdf
import plot_data_functions as pdf
import model_functions as mf
import plot_model_functions as pmf
import panelOLS_models
import spatial_error_model as sem
import spatial_error_model_new as semnew
import os
import pycountry
from collections import defaultdict
import json
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

#%%
years = list(range(2003, 2017))
directory = "/home/sara/Documents/Immigration/Shared_models/Spain/Paper_%d_%d" % (
    years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)

complete = pd.read_table("Data/spain_working_aut_comm.tsv", sep="\t", index_col = 0)
y = bdf.pivot(complete, "Country", "Value")
# Sort the Province col by alphabetic order
y = y.sortlevel()
# Replace all the 0s with the value 1 so to not produce -inf in the method computation
y.replace({0: 1}, inplace=True)
#y.head()

#%%
comunidades = y.index.levels[0].tolist()

for t in y.index.levels[1]:
    y.loc[("Spain", t), :] = y.loc[(comunidades, t), :].sum()

# Just a check.. Spain is now present as province!
#y.loc[("Spain", slice(None)),]

#%%
temp = pd.read_table("Data/xs_aut_comm.tsv", sep="\t",
                     index_col=["Province", "Year"])
xs = pd.DataFrame(columns=["Province", "Year"]+temp.columns.tolist())
xs = xs.set_index(["Province", "Year"])

for t in temp.index.levels[1]:
    xs.loc[("Spain", t), :] = temp.loc[(comunidades, t), :].sum()

palette = ['blue', 'darkgreen', 'yellowgreen', 'orange', 'lightcoral',
           'red', 'paleturquoise', 'deepskyblue', 'mediumpurple', 'fuchsia']

'''countries_list = ["Romania", "Morocco", "Albania", "Tunisia",
                  "Egypt", "Ecuador", "Peru", "China", "Philippines"]'''

#countries_list = ['China', 'Colombia', 'Ecuador', 'Germany', 'Morocco', 'Romania']

#countries_list = ['Ecuador', 'Germany', 'Morocco', 'Peru', 'Poland', 'Romania']
countries_list = ['Germany', 'Morocco', 'Peru', 'Poland', 'Romania']

countries_list_iso3 = [pycountry.countries.get(
    name=country).alpha_3 for country in countries_list]
target = "Spain"
# number of features to select
ks = [3, 5, 7, 10, 15]

y_hat, models = mf.compute_regression_model(
    y, xs, years, countries_list, target, ks)

#y_hat.to_csv(directory+"/predicted_spain.tsv", sep="\t")

#%%
pdf.relation_plot_time_variant_intern_function(y_hat, countries_list_iso3, years, ["Predicted"], complete.groupby(["Country", "Year"]), plt.figure(
    1, figsize=(15, 14)), 231, 45, palette, None, "Immigrant Stock Real VS Predicted in Spain", True, directory+"/regression_model_spain", False)

y_spain_pred = y.copy()
for country in countries_list_iso3:
    y_spain_pred.loc[("Spain", years), country] = np.array(
        y_hat.loc[(slice(None), country), "Predicted"].values, dtype=np.float32)

for k1 in models.keys():
    models[k1]["coefficients"] = list(models[k1]["coefficients"])

res_it = defaultdict(dict)

for k1 in models.keys():
    for k2, v in zip(models[k1]["features"], models[k1]["coefficients"]):
        res_it[k1][k2] = v

with open(directory+"/regression_model_spain.txt", 'w') as outfile:
    json.dump(res_it, outfile)

#%%
xs_zones = pd.read_table("Data/xs_aut_comm.tsv", sep="\t",
                         index_col=["Province", "Year"])
xs_zones = pd.concat([xs_zones, xs])
# Distance matrix related to the interested locations (regions capitals)
temp_W = pd.read_table("Data/dist_matrix.tsv", sep="\t", index_col=0)

# Add Spain distance info as mean of the 19 zones
temp_W["Spain"] = [temp_W.loc[z].mean() for z in temp_W.index]
temp_W.loc["Spain"] = [temp_W.loc[z].mean() for z in temp_W.index] + [0]
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


########################################################################################

#%%
test_size = 3
for c in countries_list:
    print("------------------------------- %s -------------------------------" % c)
    res_pred, res_est, res_params = semnew.run_model(y, c, years, "Spain", xs_zones, temp_W, temp_W.columns.tolist(
    ), False, palette, "Spatial Error Model", save=True, title_add=" in Spanish Autonomous Communities", path=directory+"/spatial_autocorr_model_%s_" % c.lower(), data_hat=y_spain_pred, train_test=True, test_size=test_size)
    res_pred.to_csv(
        directory+"/spatial_autocorr_model_fitted_values_%s.tsv" % c.lower(), sep='\t')
    res_est.to_csv(
        directory+"/spatial_autocorr_model_est_params2_%s.tsv" % c.lower(), sep='\t')
    res_params.to_csv(
        directory+"/spatial_autocorr_model_est_params1_%s.tsv" % c.lower(), sep='\t')


