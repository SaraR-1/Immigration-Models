import pandas as pd
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from collections import defaultdict
import build_data_functions as bdf
from linearmodels.panel  import PanelOLS, FirstDifferenceOLS
import plot_model_functions as pmf
import statsmodels.api as sm
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression
import pycountry
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.preprocessing import normalize

from sklearn.model_selection import train_test_split, ShuffleSplit, cross_val_score
from scipy.stats import normaltest

def panel_regression(y, xs, years, country, list_x, prev = 0, show = False, save = True, path = "", diff = False, constant = False, entity_effects = False):
    data = bdf.filter_origin_country_dataset(y, country, years, xs.index.levels[0].tolist(), xs, prev)
    if constant == False:
        exog = data[list_x]
    else:
        exog = sm.add_constant(data[list_x])
    #
    if diff == False:
            mod = PanelOLS(data.y, exog, entity_effects = entity_effects)
    else:
        mod = FirstDifferenceOLS(data.y, exog)
    res = mod.fit()
    #print("The R-squared of the regression model is %f." %res.rsquared)
    #print("Estimated parameters:")
    #print(pd.DataFrame(res.params))

    evaluation(data, res.fitted_values, constant, len(xs.columns.tolist()))

    if show == True:
            pmf.plot_real_VS_prediction(y, res.fitted_values, xs, years, country, 45, "Regression model", save, path)
    else:
        pass

    return(res.params, res.fitted_values)


def panel_regression_training_test(y, xs, years_training, years_test, country, list_x, prev = 0, show = False, save = True, path = "", diff = False, constant = False, entity_effects = False):
    years = years_training + years_test
    data = bdf.filter_origin_country_dataset(y, country, years, xs.index.levels[0].tolist(), xs, prev)

    data_tr = data.loc[(slice(None), years_training), :]
    data_te = data.loc[(slice(None), years_test), :]

    if constant == False:
        exog_tr = data_tr[list_x]
        exog_te = data_te[list_x]
    else:
        exog_tr = sm.add_constant(data_tr[list_x])
        exog_te = sm.add_constant(data_te[list_x])
    #
    if diff == False:
            mod = PanelOLS(data_tr.y, exog_tr, entity_effects = entity_effects)
    else:
        mod = FirstDifferenceOLS(data_tr.y, exog_tr)
    res_tr = mod.fit()

    #print("---------------- Training Results ----------------")
    #evaluation(data_tr, res_tr.fitted_values, constant)

    fitted_values_te = res_tr.params.values*exog_te
    fitted_values_te["fitted_values"] = fitted_values_te.sum(axis=1)
    fitted_values_ = fitted_values_te.append(res_tr.fitted_values)
    fitted_values_ = fitted_values_.sort_index()
    if show == True:
        pmf.plot_real_VS_prediction(y, fitted_values_, xs, years, country, 45, "Regression model", save = save, path = "")
    else:
        pass

    print("-------------- Trainin-Test  Results --------------")
    evaluation(data, fitted_values_, constant, len(xs.columns.tolist()))

    return(res_tr.params, fitted_values_)

def evaluation(data, y_hat, constant, k):
    if constant == False:
        R2 = 1 - (sum(np.subtract(data["y"].values, y_hat.fitted_values.values)**2) / sum((data["y"].values)**2))
    else:
        R2 = 1 - (sum(np.subtract(data["y"].values, y_hat.fitted_values.values)**2) / sum((data["y"].values - np.mean(data["y"].values))**2))

    print("R-squared %f." %round(R2,3))
    # k: number of independet vars
    n = len(data["y"].values)
    #R2_adj = 1 - (1 - R2)*((n - 1)/(n - k -1))
    #print("Adjusted R-squared %f." %round(R2_adj, 3))

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


def mse_best_model(X, y, score_list, k, models):
    '''
    Function that perform the cv of different models and compute the mse
    Input:
    - X: features to used in the model
    - y: target
    - score_list: list of score for each feature, it is used to perform the feature selection
    - models: list of models to use
    Output:
    - best mse and correspondent model and selected features
    '''
    features_list = [X.columns[idx] for idx in [list(abs(score_list)).index(i) for i in sorted(abs(score_list), reverse=True)[:k]]]

    X_ = X[features_list]
    y_ = y

    for reg in models:
        cv = ShuffleSplit(n_splits=10, test_size=0.3, random_state=0)
        vars()[str(reg).split("(")[0]] = [np.mean(cross_val_score(reg, X_, y_, cv=cv, scoring = "neg_mean_squared_error")),
                                  np.mean(cross_val_score(reg, X_, y_, cv=cv, scoring = "neg_mean_absolute_error")),
                                  np.mean(cross_val_score(reg, X_, y_, cv=cv, scoring = "r2"))]


    mse = []
    for reg in models:
        mse.append(abs(vars()[str(reg).split("(")[0]][0]))


    return [str(models[mse.index(min(mse))]).split("(")[0], min(mse), features_list]


def compute_regression_model(y, xs, years, country_list, target, ks):
    countries_list_iso3 = [pycountry.countries.get(name=country).alpha_3 for country in country_list]

    idx = pd.MultiIndex.from_product([countries_list_iso3,
                                      years],
                                     names=["Country", "Year"])
    col = ["Predicted"]
    prediction_df = pd.DataFrame('-', idx, col)

    for country in countries_list_iso3:
        #country = pycountry.countries.get(name=c).alpha_3
        '''temp = xs_additional.loc[(years, country), :]
        temp.index = temp.index.droplevel(1)
        temp = pd.concat([temp for i in range(len(xs.index.levels[0].tolist())) ], keys=xs.index.levels[0].tolist(), names=['Province'])

        xs_plus = xs.copy()
        xs_plus = pd.concat([xs_plus, temp], axis=1)

        df = bdf.filter_origin_country_dataset(y, country, years, [target], xs_plus, 2)'''

        df = bdf.filter_origin_country_dataset(y, country, years, [target], xs, 2)
        df = df.reset_index(level=0, drop=True)

        X = df.drop(["y"], axis = 1)
        y_temp = df["y"]

        f_regression_norm = normalize((f_regression(X, y_temp)[0]).reshape(1,-1))[0]
        mutual_info_regression_norm = normalize(mutual_info_regression(X, y_temp).reshape(1,-1))[0]

        scorers_aggregation = sum([f_regression_norm, mutual_info_regression_norm])

        scorers_aggregation_norm = normalize(scorers_aggregation.reshape(1,-1))[0]

        scorers_list = ["f_regression_norm", "mutual_info_regression_norm", "scorers_aggregation_norm"]

        models_function = [linear_model.LinearRegression(normalize=True),
                           linear_model.LassoCV(alphas=[0.01, 0.05, 0.1, 1], normalize=True),
                           linear_model.RidgeCV(alphas=[0.01, 0.05, 0.1, 1], normalize=True),
                           linear_model.BayesianRidge(normalize=True),
                           linear_model.ARDRegression(normalize=True)]

        model = []
        mse = []
        features = []
        for scorer in scorers_list:
            #print(scorer)
            model_temp_k = []
            mse_temp_k = []
            features_temp_k = []
            for k in ks:
                temp = mse_best_model(X, y_temp, vars()[scorer], k, models_function)
                model_temp_k.append(temp[0])
                mse_temp_k.append(temp[1])
                features_temp_k.append(temp[2])

            model.append(model_temp_k[mse_temp_k.index(min(mse_temp_k))])
            mse.append(min(mse_temp_k))
            features.append(features_temp_k[mse_temp_k.index(min(mse_temp_k))])

        model = model[mse.index(min(mse))]
        features = features[mse.index(min(mse))]


        clf = [reg for reg in models_function if model == str(reg).split("(")[0]][0].fit(X[features], y_temp)
        prediction = clf.predict(X[features])

        prediction_df.loc[(country, years), "Predicted"] = prediction
        print(country)
        print(features)
    #prediction_df.index = years
    prediction_df = prediction_df.swaplevel()
    prediction_df = prediction_df.sort_index()

    return(prediction_df)
