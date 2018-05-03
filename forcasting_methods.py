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
countries_list = ["Romania", "Morocco", "Albania", "Tunisia",
                  "Egypt", "Ecuador", "Peru", "China", "Philippines"]

palette = ['blue', 'darkgreen', 'yellowgreen', 'orange', 'lightcoral',
           'red', 'paleturquoise', 'deepskyblue', 'mediumpurple', 'fuchsia']


#%%
directory = "/home/sara/Documents/Immigration/Shared_models/SMA_%d_%d" % (
    years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)

# Forecast in SMA: last 3 years per territory
SMA_validation = pd.DataFrame(
    '-', countries_list, ["MAE", "MPE", "MAPE"])

forecast_year = 3

for c in countries_list:
    SMA_df = ff.SMA(y, c, years, zones, forecast_year)
    SMA_df.to_csv(
        directory+"/SMA_fitted_values_%s.csv" % c.lower(), sep='\t')

    a = y.loc[(zones, years), pycountry.countries.get(
        name=c).alpha_3].values
    f = SMA_df["SMA %s years" % str(len(years) - forecast_year)].values

    SMA_validation.loc[c]["MAE"] = sum(np.abs(np.subtract(a[-forecast_year:],
                                                          f[-forecast_year:])))/forecast_year
    SMA_validation.loc[c]["MPE"] = 100*sum(np.subtract(a[-forecast_year:],
                                                       f[-forecast_year:])/a[-forecast_year:])/forecast_year
    SMA_validation.loc[c]["MAPE"] = 100*sum(np.abs(np.subtract(a[-forecast_year:],
                                                           f[-forecast_year:])/a[-forecast_year:]))/forecast_year

    y_ = y.rename(columns={pycountry.countries.get(
        name=c).alpha_3: "Value"})
    y_ = y_["Value"]
    y_ = y_.reset_index(level=['Province', 'Year'])

    SMA_df.index = SMA_df.index.swaplevel(0, 1)
    SMA_df.sort_index(inplace=True)

    pdf.relation_plot_time_variant(SMA_df, SMA_df.columns.tolist(
    ), y_, zones, 45, "SMA in %s" %c, palette, save=True, path=directory+"/SMA_%s_" %c.lower(), sub_iteration=False, double_scale_x=False)

#%%
SMA_validation.to_csv(
    directory+"/SMA_metrics.csv", sep='\t')

#%%
directory = "/home/sara/Documents/Immigration/Shared_models/ES_%d_%d" % (
    years[0], years[-1])
if not os.path.exists(directory):
    os.makedirs(directory)

alphas = [.5, .65, .8, .95]

idx = pd.MultiIndex.from_product(
    [["MAE", "MPE", "MAPE"], alphas], names=['Metric', 'Alpha'])
ES_validation = pd.DataFrame("-", countries_list, idx)

# Forecasting period: all period but one (the first time has to be known)
for c in countries_list:
    es_df = ff.exp_smoothing(y, c, years, zones, alphas)

    es_df.to_csv(
        directory+"/ES_fitted_values_%s.csv" % c.lower(), sep='\t')

    a = y.loc[(zones, years), pycountry.countries.get(
        name=c).alpha_3].values
    for alpha in alphas:
        f = es_df["Exp Smoothing %s alpha" % str(alpha)].values

        ES_validation.loc[c][("MAE", alpha)] = sum(np.abs(np.subtract(a[1:],
                                                            f[1:])))/len(a[1:])
        ES_validation.loc[c][("MPE", alpha)] = 100*sum(np.subtract(a[1:],
                                                        f[1:])/a[1:])/len(a[1:])
        ES_validation.loc[c][("MAPE", alpha)] = 100*sum(np.abs(np.subtract(a[1:],
                                                                f[1:])/a[1:]))/len(a[1:])

    y_ = y.rename(columns={pycountry.countries.get(
        name=c).alpha_3: "Value"})
    y_ = y_["Value"]
    y_ = y_.reset_index(level=['Province', 'Year'])

    es_df.index = es_df.index.swaplevel(0, 1)
    es_df.sort_index(inplace=True)

    pdf.relation_plot_time_variant(es_df, es_df.columns.tolist(
    ), y_, zones, 45, "Exp Smoothing %s" %c, palette, save=True, path=directory+"/ES_%s_" % c.lower(), sub_iteration=False, double_scale_x=False)


#%%
ES_validation.to_csv(
    directory+"/ES_metrics.csv", sep='\t')
