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
import statsmodels.api as sm
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression
import pycountry
import os
from sys import argv
from collections import defaultdict
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.preprocessing import normalize

from sklearn.model_selection import train_test_split, ShuffleSplit, cross_val_score
from scipy.stats import normaltest


# In[2]:


first, last = argv[0], argv[1]
years = list(range(first, last))
#years = list(range(2005, 2017))


# In[6]:


directory = "/home/sara/Documents/Immigration/Shared_models/Plot_%d_%d" %(years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)

y = pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/resident_foreigners_norm.csv", sep = "\t", index_col=0)
y = y.groupby(["Province", "Country", "Year"], as_index=False)["Value"].sum()
y = bdf.pivot(y, "Country", "Value")

resident_foreigners_norm = pd.read_table("/home/sara/Documents/Immigration/Shared_statistics/Data_final/resident_foreigners_norm.csv")

# ## Italian Stock Prediction

# To get the Italy info we need to sum the 5 Italian zones
zones = list(pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/x_zones.csv", sep = "\t", index_col=["Province", "Year"]).index.levels[0])

for t in y.index.levels[1]:
    y.loc[("Italia", t), :] = y.loc[(zones, t), :].sum()


# In[8]:


temp = pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/x_zones.csv", sep = "\t", index_col=["Province", "Year"])
xs = pd.DataFrame(columns=["Province", "Year"]+temp.columns.tolist())
xs = xs.set_index(["Province","Year"])

for t in temp.index.levels[1]:
    xs.loc[("Italia", t), :] = temp.loc[(zones, t), :].sum()


# In[9]:


palette = ['blue', 'darkgreen', 'yellowgreen', 'orange', 'lightcoral', 'red', 'paleturquoise', 'deepskyblue', 'mediumpurple', 'fuchsia']


# In[10]:


countries_list = ["Romania", "Morocco", "Albania", "Tunisia", "Egypt", "Ecuador", "Peru", "China", "Philippines"]
countries_list_iso3 = [pycountry.countries.get(name=country).alpha_3 for country in countries_list]
target = "Italia"
# number of features to select
ks = [3, 5, 7, 10, 15]


# In[11]:


y_hat, models = mf.compute_regression_model(y, xs, years, countries_list, target, ks)


# In[12]:


pdf.relation_plot_time_variant_intern_function(y_hat, countries_list_iso3, years, ["Predicted"], resident_foreigners_norm.groupby(["Country", "Year"]), plt.figure(1, figsize=(15,14)), 331, 45, palette, None, "Immigrant Stock Real VS Predicted", True, directory+"/regression_model_italy", False)


# In[13]:


y_italia_pred = y.copy()
for country in countries_list_iso3:
    y_italia_pred.loc[("Italia", years), country] = np.array(y_hat.loc[(slice(None), country), "Predicted"].values, dtype=np.float32)


# In[14]:


for k1 in models.keys():
    models[k1]["coefficients"] = list(models[k1]["coefficients"])


# In[15]:


import json
with open(directory+"/regression_model_italy.txt", 'w') as outfile:
    json.dump(models, outfile)


# ## Zones Prediction - H. Jayet et al. paper

# In[16]:


xs_zones = pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/x_zones.csv", sep = "\t", index_col=["Province", "Year"])
xs_zones = pd.concat([xs_zones, xs])
zones_data = pd.read_table("/home/sara/Documents/Immigration/Shared_statistics/Data_final/territori.csv")
zones_data = zones_data.replace(['Provincia Autonoma Bolzano / Bozen', 'Provincia Autonoma Trento'], ['Bolzano / Bozen', 'Trento'])


# In[17]:


# Distance matrix related to the interested locations (regions capitals)
temp_W = pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/Zones_distances_matrix_mean.csv", sep = "\t", index_col=0)


# In[18]:


# Add Italy distance info as mean of the five zones
temp_W["Italia"] = [temp_W.loc[z].mean() for z in temp_W.index]
temp_W.loc["Italia"] = [temp_W.loc[z].mean() for z in temp_W.index] + [0]


# In[19]:


temp_W = (1/temp_W)**2
# w_ij = 0 if i=j
temp_W[temp_W == np.inf] = 0
# row standardization: every arow sum up to 1
temp_W = temp_W.div(temp_W.sum(axis=1), axis=0)
# Just to make sure the matrix has the right sort
temp_W = temp_W.sort_index(axis=1)
temp_W = temp_W.sort_index(axis=0)


# In[20]:


#palette = sns.color_palette()
palette = ['blue', 'darkgreen', 'yellowgreen', 'orange', 'lightcoral', 'red', 'paleturquoise', 'deepskyblue', 'mediumpurple', 'fuchsia']


# ### Romania

# In[21]:


vars_ = [["y_prev_2", "Average age of mothers at birth"],
 ["y_prev_2", "Average age of mothers at birth", "Average age of fathers at birth",
  "Free activities in voluntary associations"],
 ["y_prev_2", "Average age of mothers at birth", "Average age of fathers at birth",
  "Free activities in voluntary associations", "Communications",
  "Other goods and services"],
 ["y_prev_2", "Average age of mothers at birth", "Average age of fathers at birth",
  "Free activities in voluntary associations", "Communications",
  "Other goods and services", "Disposable Income", "reach_difficulty - Pharmacy",
  "internal_migration - Foreign country"],
 ["y_prev_2", "Average age of mothers at birth", "Average age of fathers at birth",
  "Free activities in voluntary associations", "Communications",
  "Other goods and services", "Disposable Income", "reach_difficulty - Pharmacy",
  "internal_migration - Foreign country", "Transport",
  "reach_difficulty - Emergency room", "unemployment - Total", "Born alive",
  "Clothing and footwear", "native population - Total"],
 ["y_prev_2", "Free activities in voluntary associations", "Disposable Income",
  "reach_difficulty - Emergency room", "unemployment - Total",
  "native population - Total",
  "Meetings in cultural, recreational or other associations",
  "Average monthly expenditure for housing"]]


# In[24]:


print("-------------------------------", "Romania", "-------------------------------")
res_pred, res_params = sem.run_model(y, "Romania", years, "Italia", xs_zones, temp_W, temp_W.columns.tolist(), vars_, False, palette, "Spatial Error Model", save = True, path = directory+"/spatial_autocorr_model_romania1", data_hat = y_italia_pred, train_test = True)

res_params_dict = defaultdict(dict)
for i, r in zip(["beta", "a", "rho"], res_params[:3]):
    if type(r) == np.ndarray:
        res_params_dict[i] = list(r)
    else:
        res_params_dict[i] = r

name = ['MI 3 selection','MI 5 selection', 'MI 7 selection', 'MI 10 selection', 'MI 15 selection', 'Manual selection']
for i, r, n in zip(vars_, res_params[3], name):
    for j, s in zip(i, r):
        res_params_dict[n][j] = s

with open(directory+"/spatial_autocorr_model_romania1_fitted_values_params.txt", 'w') as outfile:
    json.dump(res_params_dict, outfile)

res_pred.to_csv(directory+"/spatial_autocorr_model_romania1_fitted_values.csv", sep = "\t")


# ### Morocco

# In[21]:


vars_ = [["y_prev_2","Free activities in voluntary associations"],
 ["y_prev_2","Free activities in voluntary associations", "internal_migration - Foreign country",
  "native population - Total"],
 ["y_prev_2","Free activities in voluntary associations", "internal_migration - Foreign country",
  "native population - Total", "Free activities in non voluntary associations",
  "Meetings in cultural, recreational or other associations"],
 ["y_prev_2","Free activities in voluntary associations", "internal_migration - Foreign country",
  "native population - Total", "Free activities in non voluntary associations",
  "Meetings in cultural, recreational or other associations", "internal_migration - Italy",
  "political_info - Some times in a week", "Pay money to an association"],
 ["y_prev_2","Free activities in voluntary associations", "internal_migration - Foreign country",
  "native population - Total", "Free activities in non voluntary associations",
  "Meetings in cultural, recreational or other associations", "internal_migration - Italy",
  "political_info - Some times in a week", "Pay money to an association", "reach_difficulty - Supermarket",
  "reach_difficulty - Post offices", "Born alive", "Disposable Income", "political_info - Every day"],
 ["y_prev_2", "Free activities in voluntary associations", "native population - Total",
  "Meetings in cultural, recreational or other associations", "Disposable Income",
  "Average monthly expenditure for housing", "unemployment - Total", "reach_difficulty - Emergency room"]]


# In[22]:


print("-------------------------------", "Morocco", "-------------------------------")
res_pred, res_params = sem.run_model(y, "Morocco", years, "Italia", xs_zones, temp_W, temp_W.columns.tolist(), vars_, False, palette, "Spatial Error Model", save = True, path = directory+"/spatial_autocorr_model_Morocco1", data_hat = y_italia_pred, train_test = True)

res_params_dict = defaultdict(dict)
for i, r in zip(["beta", "a", "rho"], res_params[:3]):
    if type(r) == np.ndarray:
        res_params_dict[i] = list(r)
    else:
        res_params_dict[i] = r

name = ['MI 3 selection','MI 5 selection', 'MI 7 selection', 'MI 10 selection', 'MI 15 selection', 'Manual selection']
for i, r, n in zip(vars_, res_params[3], name):
    for j, s in zip(i, r):
        res_params_dict[n][j] = s

with open(directory+"/spatial_autocorr_model_morocco1_fitted_values_params.txt", 'w') as outfile:
    json.dump(res_params_dict, outfile)

res_pred.to_csv(directory+"/spatial_autocorr_model_Morocco1_fitted_values.csv", sep = "\t")


# ### Albania

# In[24]:


vars_ = [["y_prev_2", "native population - Total"],
 ["y_prev_2", "native population - Total",  "internal_migration - Foreign country",
  "Free activities in voluntary associations"],
 ["y_prev_2", "native population - Total",  "internal_migration - Foreign country",
  "Free activities in voluntary associations", "Disposable Income",
  "political_info - Every day"],
 ["y_prev_2", "native population - Total",  "internal_migration - Foreign country",
  "Free activities in voluntary associations", "Disposable Income",
  "political_info - Every day", "reach_difficulty - Supermarket", "Born alive",
  "Free activities in non voluntary associations"],
 ["y_prev_2", "native population - Total",  "internal_migration - Foreign country",
  "Free activities in voluntary associations", "Disposable Income",
  "political_info - Every day", "reach_difficulty - Supermarket", "Born alive",
  "Free activities in non voluntary associations", "reach_difficulty - Pharmacy",
  "political_info - Never", "political_info - Some times in a week",
  "Pay money to an association", "Meetings in cultural, recreational or other associations"]
 ["y_prev_2", "native population - Total", "Free activities in voluntary associations",
  "Disposable Income", "Meetings in cultural, recreational or other associations",
  "Average monthly expenditure for housing", "unemployment - Total", "reach_difficulty - Emergency room"]]


# In[25]:


print("-------------------------------", "Albania", "-------------------------------")
res_pred, res_params = sem.run_model(y, "Albania", years, "Italia", xs_zones, temp_W, temp_W.columns.tolist(), vars_, False, palette, "Spatial Error Model", save = True, path = directory+"/spatial_autocorr_model_albania1", data_hat = y_italia_pred, train_test = True)

res_params_dict = defaultdict(dict)
for i, r in zip(["beta", "a", "rho"], res_params[:3]):
    if type(r) == np.ndarray:
        res_params_dict[i] = list(r)
    else:
        res_params_dict[i] = r

name = ['MI 3 selection','MI 5 selection', 'MI 7 selection', 'MI 10 selection', 'MI 15 selection', 'Manual selection']
for i, r, n in zip(vars_, res_params[3], name):
    for j, s in zip(i, r):
        res_params_dict[n][j] = s

with open(directory+"/spatial_autocorr_model_albania1_fitted_values_params.txt", 'w') as outfile:
    json.dump(res_params_dict, outfile)

res_pred.to_csv(directory+"/spatial_autocorr_model_albania1_fitted_values.csv", sep = "\t")


# ### Tunisia

# In[27]:


vars_ = [["y_prev_2", "Pay money to an association"],
 ["y_prev_2", "Pay money to an association", "internal_migration - Foreign country",
  "native population - Total"],
 ["y_prev_2", "Pay money to an association", "internal_migration - Foreign country",
  "native population - Total", "Free activities in voluntary associations",
  "Meetings in cultural, recreational or other associations"],
 ["y_prev_2", "Pay money to an association", "internal_migration - Foreign country",
  "native population - Total", "Free activities in voluntary associations",
  "Meetings in cultural, recreational or other associations",
  "Free activities in non voluntary associations", "reach_difficulty - Post offices",
  "political_info - Never"],
 ["y_prev_2", "Pay money to an association", "internal_migration - Foreign country",
  "native population - Total", "Free activities in voluntary associations",
  "Meetings in cultural, recreational or other associations",
  "Free activities in non voluntary associations", "reach_difficulty - Post offices",
  "political_info - Never", "internal_migration - Italy", "reach_difficulty - Pharmacy",
  "Born alive", "Accommodation and catering services", "Political_info - Every day"],
 ["y_prev_2", "native population - Total", "Free activities in voluntary associations",
  "Meetings in cultural, recreational or other associations", "Disposable Income",
  "Average monthly expenditure for housing", "unemployment - Total", "reach_difficulty - Emergency room"]]


# In[28]:


print("-------------------------------", "Tunisia", "-------------------------------")
res_pred, res_params = sem.run_model(y, "Tunisia", years, "Italia", xs_zones, temp_W, temp_W.columns.tolist(), vars_, False, palette, "Spatial Error Model", save = True, path = directory+"/spatial_autocorr_model_tunisia1", data_hat = y_italia_pred, train_test = True)

res_params_dict = defaultdict(dict)
for i, r in zip(["beta", "a", "rho"], res_params[:3]):
    if type(r) == np.ndarray:
        res_params_dict[i] = list(r)
    else:
        res_params_dict[i] = r

name = ['MI 3 selection','MI 5 selection', 'MI 7 selection', 'MI 10 selection', 'MI 15 selection', 'Manual selection']
for i, r, n in zip(vars_, res_params[3], name):
    for j, s in zip(i, r):
        res_params_dict[n][j] = s

with open(directory+"/spatial_autocorr_model_tunisia1_fitted_values_params.txt", 'w') as outfile:
    json.dump(res_params_dict, outfile)

res_pred.to_csv(directory+"/spatial_autocorr_model_tunisia1_fitted_values.csv", sep = "\t")


# ### Egypt

# In[30]:


vars_ = [["y_prev_2", "native population - Total"],
 ["y_prev_2", "native population - Total", "Pay money to an association", "Non food"],
 ["y_prev_2", "native population - Total", "Pay money to an association", "Non food",
  "internal_migration - Foreign country", "Free activities in voluntary associations"],
 ["y_prev_2", "native population - Total", "Pay money to an association", "Non food",
  "internal_migration - Foreign country", "Free activities in voluntary associations",
  "internal_migration - Italy", "reach_difficulty - Post offices",
  "Meetings in cultural, recreational or other associations"],
 ["y_prev_2", "native population - Total", "Pay money to an association", "Non food",
  "internal_migration - Foreign country", "Free activities in voluntary associations",
  "internal_migration - Italy", "reach_difficulty - Post offices",
  "Meetings in cultural, recreational or other associations",
  "Other goods and services",  "Communications", "Food and non-alcoholic beverages",
  "Accommodation and catering services", "Transport"],
 ["y_prev_2", "native population - Total", "Free activities in voluntary associations",
  "Meetings in cultural, recreational or other associations", "Disposable Income",
  "Average monthly expenditure for housing", "unemployment - Total",
  "reach_difficulty - Emergency room"]]


# In[31]:


print("-------------------------------", "Egypt", "-------------------------------")
res_pred, res_params = sem.run_model(y, "Egypt", years, "Italia", xs_zones, temp_W, temp_W.columns.tolist(), vars_, False, palette, "Spatial Error Model", save = True, path = directory+"/spatial_autocorr_model_egypt1", data_hat = y_italia_pred, train_test = True)

res_params_dict = defaultdict(dict)
for i, r in zip(["beta", "a", "rho"], res_params[:3]):
    if type(r) == np.ndarray:
        res_params_dict[i] = list(r)
    else:
        res_params_dict[i] = r

name = ['MI 3 selection','MI 5 selection', 'MI 7 selection', 'MI 10 selection', 'MI 15 selection', 'Manual selection']
for i, r, n in zip(vars_, res_params[3], name):
    for j, s in zip(i, r):
        res_params_dict[n][j] = s

with open(directory+"/spatial_autocorr_model_egypt1_fitted_values_params.txt", 'w') as outfile:
    json.dump(res_params_dict, outfile)

res_pred.to_csv(directory+"/spatial_autocorr_model_egypt1_fitted_values.csv", sep = "\t")


# ### Ecuador

# In[ ]:


vars_ = [["y_prev_2", "native population - Total"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Pay money to an association"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Pay money to an association", "reach_difficulty - Post offices",
  "Free activities in voluntary associations"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Pay money to an association", "reach_difficulty - Post offices",
  "Free activities in voluntary associations", "internal_migration - Italy",
  "Accommodation and catering services",
  "Meetings in cultural, recreational or other associations"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Pay money to an association", "reach_difficulty - Post offices",
  "Free activities in voluntary associations", "internal_migration - Italy",
  "Accommodation and catering services",
  "Meetings in cultural, recreational or other associations",
  "Other goods and services", "Non food", "reach_difficulty - Supermarket",
  "Transport", "Disposable Income"],
 ["y_prev_2", "native population - Total", "Free activities in voluntary associations",
  "Meetings in cultural, recreational or other associations", "Disposable Income",
  "Average monthly expenditure for housing", "unemployment - Total",
  "reach_difficulty - Emergency room"]]


# In[ ]:


print("-------------------------------", "Ecuador", "-------------------------------")
res_pred, res_params = sem.run_model(y, "Ecuador", years, "Italia", xs_zones, temp_W, temp_W.columns.tolist(), vars_, False, palette, "Spatial Error Model", save = True, path = directory+"/spatial_autocorr_model_ecuador1", data_hat = y_italia_pred, train_test = True)

res_params_dict = defaultdict(dict)
for i, r in zip(["beta", "a", "rho"], res_params[:3]):
    if type(r) == np.ndarray:
        res_params_dict[i] = list(r)
    else:
        res_params_dict[i] = r

name = ['MI 3 selection','MI 5 selection', 'MI 7 selection', 'MI 10 selection', 'MI 15 selection', 'Manual selection']
for i, r, n in zip(vars_, res_params[3], name):
    for j, s in zip(i, r):
        res_params_dict[n][j] = s

with open(directory+"/spatial_autocorr_model_ecuador1_fitted_values_params.txt", 'w') as outfile:
    json.dump(res_params_dict, outfile)

res_pred.to_csv(directory+"/spatial_autocorr_model_ecuador1_fitted_values.csv", sep = "\t")


# ### Peru

# In[ ]:


vars_ = [["y_prev_2", "native population - Total"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Free activities in voluntary associations"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Free activities in voluntary associations", "Pay money to an association",
  "Disposable Income"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Free activities in voluntary associations", "Pay money to an association",
  "Disposable Income", "internal_migration - Italy", "reach_difficulty - Post offices",
  "Meetings in cultural, recreational or other associations"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Free activities in voluntary associations", "Pay money to an association",
  "Disposable Income", "internal_migration - Italy", "reach_difficulty - Post offices",
  "Meetings in cultural, recreational or other associations",
  "reach_difficulty - Supermarket", "Non food", "Born alive",
  "political_info - Every day", "Free activities in non voluntary associations"],
 ["y_prev_2", "native population - Total", "Free activities in voluntary associations",
  "Disposable Income", "Meetings in cultural, recreational or other associations",
  "Average monthly expenditure for housing", "unemployment - Total",
  "reach_difficulty - Emergency room"]]


# In[ ]:


print("-------------------------------", "Peru", "-------------------------------")
res_pred, res_params = sem.run_model(y, "Peru", years, "Italia", xs_zones, temp_W, temp_W.columns.tolist(), vars_, False, palette, "Spatial Error Model", save = True, path = directory+"/spatial_autocorr_model_peru1", data_hat = y_italia_pred, train_test = True)

res_params_dict = defaultdict(dict)
for i, r in zip(["beta", "a", "rho"], res_params[:3]):
    if type(r) == np.ndarray:
        res_params_dict[i] = list(r)
    else:
        res_params_dict[i] = r

name = ['MI 3 selection','MI 5 selection', 'MI 7 selection', 'MI 10 selection', 'MI 15 selection', 'Manual selection']
for i, r, n in zip(vars_, res_params[3], name):
    for j, s in zip(i, r):
        res_params_dict[n][j] = s

with open(directory+"/spatial_autocorr_model_peru1_fitted_values_params.txt", 'w') as outfile:
    json.dump(res_params_dict, outfile)

res_pred.to_csv(directory+"/spatial_autocorr_model_peru1_fitted_values.csv", sep = "\t")


# ### China

# In[ ]:


vars_ = [["y_prev_2", "Born alive"],
 ["y_prev_2", "Born alive", "internal_migration - Foreign country",
  "political_info - Some times in a week"],
 ["y_prev_2", "Born alive", "internal_migration - Foreign country",
  "political_info - Some times in a week""reach_difficulty - Pharmacy",
  "Free activities in voluntary associations"],
 ["y_prev_2", "Born alive", "internal_migration - Foreign country",
  "political_info - Some times in a week""reach_difficulty - Pharmacy",
  "Free activities in voluntary associations", "reach_difficulty - Post offices",
  "political_info - Every day",
  "Meetings in cultural, recreational or other associations"],
 ["y_prev_2", "Born alive", "internal_migration - Foreign country",
  "political_info - Some times in a week""reach_difficulty - Pharmacy",
  "Free activities in voluntary associations", "reach_difficulty - Post offices",
  "political_info - Every day",
  "Meetings in cultural, recreational or other associations",
  "native population - Total", "reach_difficulty - Emergency room", "Disposable Income",
  "Pay money to an association", "Average age of fathers at birth"],
 ["y_prev_2", "Free activities in voluntary associations",
  "Meetings in cultural, recreational or other associations",
  "native population - Total", "reach_difficulty - Emergency room",
  "Disposable Income", "Average monthly expenditure for housing",
  "unemployment - Total"]]


# In[ ]:


print("-------------------------------", "China", "-------------------------------")
res_pred, res_params = sem.run_model(y, "China", years, "Italia", xs_zones, temp_W, temp_W.columns.tolist(), vars_, False, palette, "Spatial Error Model", save = True, path = directory+"/spatial_autocorr_model_china1", data_hat = y_italia_pred, train_test = True)

res_params_dict = defaultdict(dict)
for i, r in zip(["beta", "a", "rho"], res_params[:3]):
    if type(r) == np.ndarray:
        res_params_dict[i] = list(r)
    else:
        res_params_dict[i] = r

name = ['MI 3 selection','MI 5 selection', 'MI 7 selection', 'MI 10 selection', 'MI 15 selection', 'Manual selection']
for i, r, n in zip(vars_, res_params[3], name):
    for j, s in zip(i, r):
        res_params_dict[n][j] = s

with open(directory+"/spatial_autocorr_model_china1_fitted_values_params.txt", 'w') as outfile:
    json.dump(res_params_dict, outfile)

res_pred.to_csv(directory+"/spatial_autocorr_model_china1_fitted_values.csv", sep = "\t")


# ### Philippines

# In[ ]:


vars_ = [["y_prev_2", "native population - Total"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Other goods and services"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Other goods and services", "Communications", "Non food"],
 ["y_prev_2", "native population - Total", "internal_migration - Foreign country",
  "Other goods and services", "Communications", "Non food",
  "Housing, water, electricity, gas and other fuels",
  "Accommodation and catering services", "Free activities in voluntary associations"],
 ["y_prev_2", "Other goods and services", "internal_migration - Foreign country",
  "native population - Total", "Communications",
  "Non food", "Housing, water, electricity, gas and other fuels", "Accommodation and catering services",
  "Free activities in voluntary associations",
  "reach_difficulty - Post offices" "Born alive", "Pay money to an association",
  "Average age of fathers at birth", "Food and non-alcoholic beverages"],
 ["y_prev_2", "native population - Total", "Free activities in voluntary associations",
  "Meetings in cultural, recreational or other associations", "Disposable Income",
  "Average monthly expenditure for housing", "unemployment - Total",
  "reach_difficulty - Emergency room"]]


# In[ ]:


print("-------------------------------", "Philippines", "-------------------------------")
res_pred, res_params = sem.run_model(y, "Philippines", years, "Italia", xs_zones, temp_W, temp_W.columns.tolist(), vars_, False, palette, "Spatial Error Model", save = True, path = directory+"/spatial_autocorr_model_philippines1", data_hat = y_italia_pred, train_test = True)

res_params_dict = defaultdict(dict)
for i, r in zip(["beta", "a", "rho"], res_params[:3]):
    if type(r) == np.ndarray:
        res_params_dict[i] = list(r)
    else:
        res_params_dict[i] = r

name = ['MI 3 selection','MI 5 selection', 'MI 7 selection', 'MI 10 selection', 'MI 15 selection', 'Manual selection']
for i, r, n in zip(vars_, res_params[3], name):
    for j, s in zip(i, r):
        res_params_dict[n][j] = s

with open(directory+"/spatial_autocorr_model_philippines1_fitted_values_params.txt", 'w') as outfile:
    json.dump(res_params_dict, outfile)

res_pred.to_csv(directory+"/spatial_autocorr_model_philippines1_fitted_values.csv", sep = "\t")
