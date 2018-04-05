import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

import numpy as np
from statsmodels.datasets import grunfeld
from linearmodels.panel  import PanelOLS
import pandas as pd
import build_data_functions as bdf
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import model_functions as mf
import plot_model_functions as pmf
import plot_data_functions as pdf
import statsmodels.api as sm
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression
import pycountry


def panel_regression(y, xs, years, country, ks, zones_data, palette, title, plot = True, unique_plot = False, save_final = True, save = False, show = False, diff = False, constant = False, entity_effects = False):
    country = pycountry.countries.get(name=country).alpha_3
    print("--------------------- Previous  Time ---------------------")
    # PanelOLS uses fixed effect (i.e., entity effects) to eliminate the entity specific components.
    # FirstDifferenceOLS takes the first difference to eliminate the entity specific effect.
    param, values = mf.panel_regression(y, xs, years, country, ['y_prev_1'], prev = 1, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)
    print(param)

    # Training - Test (2014, 2015)
    #param, values = mf.panel_regression_training_test(y, xs, years[:-2], years[-2:], country, ['y_prev_1'], prev = 1, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)

    # Training - Test (2014, 2015, 2016)
    param, values = mf.panel_regression_training_test(y, xs, years[:-3], years[-3:], country, ['y_prev_1'], prev = 1, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)
    print(param)
    results1 = pd.DataFrame(values.fitted_values)
    results1 = results1.rename(columns = {"fitted_values": "Previous time"})

    print("-------------------- Previous 2 Times --------------------")
    param, values = mf.panel_regression(y, xs, years, country, ['y_prev_1', 'y_prev_2'], prev = 2, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)
    print(param)
    # Training - Test (2014, 2015)
    #param, values = mf.panel_regression_training_test(y, xs, years[:-2], years[-2:], country, ['y_prev_1', 'y_prev_2'], prev = 2, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)

    # Training - Test (2014, 2015, 2016)
    param, values = mf.panel_regression_training_test(y, xs, years[:-3], years[-3:], country, ['y_prev_1', 'y_prev_2'], prev = 2, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)
    print(param)
    results1 = pd.concat([results1, values.fitted_values], axis = 1)
    results1 = results1.rename(columns = {"fitted_values": "Previous two times"})

    print("------------- Variable Selection  Plot based -------------")
    var_selection = ['native population - Total', 'Free activities in voluntary associations',
                     'Meetings in cultural, recreational or other associations',
                     'Disposable Income', 'Average monthly expenditure for housing',
                     'unemployment - Total', 'reach_difficulty - Emergency room']

    # PanelOLS uses fixed effect (i.e., entity effects) to eliminate the entity specific components.
    # FirstDifferenceOLS takes the first difference to eliminate the entity specific effect.
    param, values = mf.panel_regression(y, xs, years, country, ['y_prev_1', 'y_prev_2']+var_selection, prev = 2, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)
    print(param)
    # Training - Test (2014, 2015)
    #param, values = mf.panel_regression_training_test(y, xs, years[:-2], years[-2:], country, ['y_prev_1', 'y_prev_2']+var_selection, prev = 2, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)

    # Training - Test (2014, 2015, 2016)
    param, values = mf.panel_regression_training_test(y, xs, years[:-3], years[-3:], country, ['y_prev_1', 'y_prev_2']+var_selection, prev = 2, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)
    print(param)
    results1 = pd.concat([results1, values.fitted_values], axis = 1)
    results1 = results1.rename(columns = {"fitted_values": "Manual Selection"})

    print("----------------- Variable Selection  MI -----------------")
    data = bdf.filter_origin_country_dataset(y, country, years, xs.index.levels[0].tolist(), xs, prev = 2)
    y_ = data["y"]
    xs_ = data.loc[:, data.columns != 'y']

    results2 = pd.DataFrame()
    for k in ks:
        print("--------------------- k = %d ---------------------" %k)
        xs_new_ = SelectKBest(mutual_info_regression, k=k).fit_transform(xs_, y_)
        selected_ = []
        for v in xs_new_[0]:
            print()
            temp = (data == v).idxmax(axis=1)[0]
            selected_.append(temp)

        param, values = mf.panel_regression(y, xs, years, country, selected_, prev = 2, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)
        print(param)
        # Training - Test (2014, 2015)
        #param, values = mf.panel_regression_training_test(y, xs, years[:-2], years[-2:], country, selected_, prev = 2, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)

        # Training - Test (2014, 2015, 2016)
        param, values = mf.panel_regression_training_test(y, xs, years[:-3], years[-3:], country, selected_, prev = 2, save = save, show = show, diff = diff, constant = constant, entity_effects = entity_effects)
        print(param)
        results2 = pd.concat([results2, values.fitted_values], axis = 1)
        results2 = results2.rename(columns = {"fitted_values": "MI %d selection" %k})

    if plot == True:
        results1.index = results1.index.swaplevel(0, 1)
        results1.sort_index(inplace=True)

        results2.index = results2.index.swaplevel(0, 1)
        results2.sort_index(inplace=True)

        y_ = y.rename(columns = {country: "Value"})
        y_ = y_["Value"]
        y_ = y_.reset_index(level=['Province', 'Year'])

        if unique_plot == True:
            results1 = pd.concat([results1, results2], axis = 1)
            pdf.relation_plot_time_variant(results1, results1.columns.tolist(), y_, zones_data, 45, title, palette, save_final, "Plots/"+"_".join(title.lower().split(" ")), sub_iteration=False, double_scale_x = False)
        else:
            temp = " ".join([title, str(1)])
            pdf.relation_plot_time_variant(results1, results1.columns.tolist(), y_, zones_data, 45, temp, palette, save_final, "Plots/"+"_".join(temp.lower().split(" ")), sub_iteration=False, double_scale_x =  False)
            temp = " ".join([title, str(2)])
            pdf.relation_plot_time_variant(results2, results2.columns.tolist(), y_, zones_data, 45, temp, palette, save_final, "Plots/"+"_".join(temp.lower().split(" ")), sub_iteration=False, double_scale_x =  False)
