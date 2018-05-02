#%%
import pandas as pd
import numpy as np
import build_data_functions as bdf
import plot_data_functions as pdf
import forcasting_functions as ff
import pycountry
import os
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

#%%
y = pd.read_table(
    "/home/sara/Documents/Immigration/Shared_models/Data/resident_foreigners_norm.csv", sep="\t", index_col=0)
y = y.groupby(["Province", "Country", "Year"], as_index=False)["Value"].sum()
y = bdf.pivot(y, "Country", "Value")

zones = list(pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/x_zones.csv",
                           sep="\t", index_col=["Province", "Year"]).index.levels[0])

years = list(range(2005, 2017))

#%%
directory = "/home/sara/Documents/Immigration/Shared_models/SMA_%d_%d" % (
    years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)

countries_list = ["Romania", "Morocco", "Albania", "Tunisia",
                  "Egypt", "Ecuador", "Peru", "China", "Philippines"]

palette = ['blue', 'darkgreen', 'yellowgreen', 'orange', 'lightcoral',
           'red', 'paleturquoise', 'deepskyblue', 'mediumpurple', 'fuchsia']

#%%
validation = pd.DataFrame('-', countries_list, ["R2", "R2_adj"])
for c in countries_list:
    SMA_df = ff.SMA(y, c, years, zones, 3)
    SMA_df.to_csv(
        directory+"/SMA_fitted_values_%s.csv" % c.lower(), sep='\t')

    y_ = y.rename(columns={pycountry.countries.get(
        name=c).alpha_3: "Value"})
    y_ = y_["Value"]
    y_ = y_.reset_index(level=['Province', 'Year'])

    pdf.relation_plot_time_variant(SMA_df, SMA_df.columns.tolist(
    ), y_, zones, 45, "SMA", palette, save=True, path=directory+"/SMA_%s_" %c.lower(), sub_iteration=False, double_scale_x=False)

#%%
directory = "/home/sara/Documents/Immigration/Shared_models/ES_%d_%d" % (
    years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)

for c in countries_list:
    es_df = ff.exp_smoothing(y, c, years, zones, [.5, .65, .8, .95])

    es_df.to_csv(
        directory+"/ES_fitted_values_%s.csv" % c.lower(), sep='\t')

    y_ = y.rename(columns={pycountry.countries.get(
        name=c).alpha_3: "Value"})
    y_ = y_["Value"]
    y_ = y_.reset_index(level=['Province', 'Year'])

    pdf.relation_plot_time_variant(es_df, es_df.columns.tolist(
    ), y_, zones, 45, "Exp Smoothing", palette, save=True, path=directory+"/ES_%s_" % c.lower(), sub_iteration=False, double_scale_x=False)
