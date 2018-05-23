#%%
import pandas as pd
import numpy as np
import sys
sys.path.append('/home/sara/Documents/Immigration/Shared_models')
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

countries_list = ['China', 'Ecuador', 'Germany',
                  'Morocco', 'Peru', 'Poland', 'Romania']

zones = list(xs.index.levels[0])

#%%
directory = "/home/sara/Documents/Immigration/Shared_models/Spain/SMA_%d_%d" % (
    years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)

# Forecast in SMA: last 3 years per territory
SMA_validation = pd.DataFrame(
    '-', countries_list, ["MAE", "MSE", "RMSE"])

forecast_year = 3

for c in countries_list:
    SMA_df = ff.SMA(y, c, years, zones, forecast_year)
    SMA_df.to_csv(
        directory+"/SMA_fitted_values_%s.tsv" % c.lower(), sep='\t')

    a = y.loc[(zones, years[-forecast_year:]), pycountry.countries.get(
        name=c).alpha_3].values
    f = SMA_df.loc[(slice(None), years[-forecast_year:]),
                   "SMA %s years" % str(len(years) - forecast_year)].values

    SMA_validation.loc[c]["MAE"] = sum(np.abs(np.subtract(a,
                                                          f)))/len(a)
    SMA_validation.loc[c]["MSE"] = round(np.mean(np.subtract(a,
                                                             f)**2), 5)
    SMA_validation.loc[c]["RMSE"] = round(
        np.sqrt(SMA_validation.loc[c]["MSE"]), 5)

    y_ = y.rename(columns={pycountry.countries.get(
        name=c).alpha_3: "Value"})
    y_ = y_["Value"]
    y_ = y_.reset_index(level=['Province', 'Year'])

    SMA_df.index = SMA_df.index.swaplevel(0, 1)
    SMA_df.sort_index(inplace=True)

    pdf.relation_plot_time_variant(SMA_df, SMA_df.columns.tolist(
    ), y_, zones, 45, "SMA in %s" % c, palette, save=True, path=directory+"/SMA_%s_" % c.lower(), sub_iteration=False, double_scale_x=False, title_add=" in Spanish Autonomous Communities")

SMA_validation.to_csv(
    directory+"/SMA_metrics.tsv", sep='\t')


#%%
directory = "/home/sara/Documents/Immigration/Shared_models/Spain/ES_%d_%d" % (
    years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)

alphas = [.5, .65, .8, .95]

idx = pd.MultiIndex.from_product(
    [["MAE", "MSE", "RMSE"], alphas], names=['Metric', 'Alpha'])
ES_validation = pd.DataFrame("-", countries_list, idx)

# Forecasting period: all period but one (the first time has to be known)
for c in countries_list:
    es_df = ff.exp_smoothing(y, c, years, zones, alphas)

    es_df.to_csv(
        directory+"/ES_fitted_values_%s.tsv" % c.lower(), sep='\t')

    a = y.loc[(zones, years[1:]), pycountry.countries.get(
        name=c).alpha_3].values
    for alpha in alphas:
        f = es_df.loc[(slice(None), years[1:]),
                      "Exp Smoothing %s alpha" % str(alpha)].values

        ES_validation.loc[c][("MAE", alpha)] = sum(np.abs(np.subtract(a,
                                                                      f)))/len(a)
        ES_validation.loc[c][("MSE", alpha)] = round(np.mean(np.subtract(a,
                                                                         f)**2), 5)
        ES_validation.loc[c][("RMSE", alpha)] = round(
            np.sqrt(ES_validation.loc[c][("MSE", alpha)]), 5)

    y_ = y.rename(columns={pycountry.countries.get(
        name=c).alpha_3: "Value"})
    y_ = y_["Value"]
    y_ = y_.reset_index(level=['Province', 'Year'])

    es_df.index = es_df.index.swaplevel(0, 1)
    es_df.sort_index(inplace=True)

    pdf.relation_plot_time_variant(es_df, es_df.columns.tolist(
    ), y_, zones, 45, "Exp Smoothing %s" % c, palette, save=True, path=directory+"/ES_%s_" % c.lower(), sub_iteration=False, double_scale_x=False, title_add=" in Spanish Autonomous Communities")

ES_validation.to_csv(
    directory+"/ES_metrics.tsv", sep='\t')
