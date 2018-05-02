import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

import pandas as pd
import numpy as np
import pycountry
import itertools
from scipy.optimize import least_squares
import math
import random
import statsmodels
from scipy.optimize import minimize
from scipy.optimize import fsolve
#from pandas.core import datetools
import statsmodels.api as sm
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from collections import defaultdict
from math import pi, e
import model_functions as mf
import build_data_functions as bdf
import plot_model_functions as pmf
import matplotlib.pyplot as plt
import plot_data_functions as pdf


def stepI(param, data_, W, times, ref_I, territories, data_hat):
    beta = param[0]
    a = param[1:-1]
    ro = param[-1]

    T = len(times)
    I = len(territories)

    identity_I = np.identity(I)
    identity_I_1 = np.identity(I-1)
    neg1 = np.negative(np.ones((I-1, 1)))
    # Not-squared matrix
    Q = np.append(identity_I_1, neg1, axis=1)
    # All the I-1 locations (all but the reference one)
    terr_not_ref = [i for i in territories if i != ref_I]

    # Modify W s.t. the "ref_I" location is the last one (so that Q is well defined)
    W = W.reindex(index = terr_not_ref+[ref_I], columns = terr_not_ref+[ref_I])

    # Time-invariant quantity
    L = Q.dot(np.linalg.inv(identity_I-ro*W)).dot(np.linalg.inv(identity_I-ro*W.T)).dot(Q.T)

    log_lik = 0

    for t in times[:]:
        if type(data_hat) != type(None):
            y = (data_.loc[(t, terr_not_ref), "y"]/data_hat.loc[(t, ref_I), "y"]).values
        else:
            y = (data_.loc[(t, terr_not_ref), "y"]/data_.loc[(t, ref_I), "y"]).values

        x = (data_.loc[(t, terr_not_ref), "y_prev_1"]/data_.loc[(t, ref_I), "y_prev_1"]).values
        #print(y.shape, x.shape, len(a))
        main_term = np.log(y) - beta*np.log(x) - a

        log_lik += np.log(np.linalg.det(L)) + main_term.T.dot(np.linalg.inv(L)).dot(main_term)

    return(log_lik)

'''def stepII(theta, a, x_, ref_I, territories):
  # All the I-1 locations (all but the reference one)
  terr_not_ref = [i for i in territories if i != ref_I]

  x_I = x_.loc[ref_I].values
  temp = np.array([(a[terr_not_ref.index(i)] - np.dot(np.subtract(x_.loc[i].values, x_I), theta)) for i in terr_not_ref])

  ols = (1/len(a))*temp.T.dot(temp)
  return(ols)


def stepII_constant(param, a, x_, ref_I, territories):
    theta = param[:-1]
    c = param[-1]
    # All the I-1 locations (all but the reference one)
    terr_not_ref = [i for i in territories if i != ref_I]

    x_I = x_.loc[ref_I].values
    temp = np.array([(a[terr_not_ref.index(i)] - np.dot(np.subtract(x_.loc[i].values, x_I), theta) - c) for i in terr_not_ref])

    ols = (1/len(a))*temp.T.dot(temp)
    return(ols)'''

'''def stepII(theta, data_, W, times, beta_, ro_, x_, ref_I, territories, data_hat):
    T = len(times)
    I = len(territories)

    identity_I = np.identity(I)
    identity_I_1 = np.identity(I-1)
    neg1 = np.negative(np.ones((I-1, 1)))
    # Not-squared matrix
    Q = np.append(identity_I_1, neg1, axis=1)
    # All the I-1 locations (all but the reference one)
    terr_not_ref = [i for i in territories if i != ref_I]

    # Modify W s.t. the "ref_I" location is the last one (so that Q is well defined)
    W = W.reindex(index = terr_not_ref+[ref_I], columns = terr_not_ref+[ref_I])

    # Time-invariant quantity
    L = Q.dot(np.linalg.inv(identity_I-ro_*W)).dot(np.linalg.inv(identity_I-ro_*W.T)).dot(Q.T)

    log_lik = 0
    x_I = x_.loc[ref_I].values
    x_i = np.array([np.dot(np.subtract(x_.loc[i].values, x_I), theta) for i in terr_not_ref])

    for t in times[:]:
        if type(data_hat) != type(None):
            y = (data_.loc[(t, terr_not_ref), "y"]/data_hat.loc[(t, ref_I), "y"]).values
        else:
            y = (data_.loc[(t, terr_not_ref), "y"]/data_.loc[(t, ref_I), "y"]).values
        x = (data_.loc[(t, terr_not_ref), "y_prev_1"]/data_.loc[(t, ref_I), "y_prev_1"]).values
        #print(y.shape, x.shape, len(a))
        main_term = x_i + np.log(y) - beta_*np.log(x)

        log_lik += np.log(np.linalg.det(L)) + main_term.T.dot(np.linalg.inv(L)).dot(main_term)

    return(log_lik)'''

def stepII(theta, a, x_, ref_I, territories, constant):
    # All the I-1 locations (all but the reference one)
    terr_not_ref = [i for i in territories if i != ref_I]
    # to be sure about the ordering
    A = [a[terr_not_ref.index(i)] for i in terr_not_ref]

    if constant:
        # with constant
        var_c = np.ones((len(A), 1))
        X = x_.loc[terr_not_ref].values - x_.loc[ref_I].values
        X = np.append(var_c, X, axis=1)
    else:
        # without constant
        X = x_.loc[terr_not_ref].values - x_.loc[ref_I].values
    # Handle matrix dependencies --> singular matrix
    try:
        temp1 = np.linalg.inv(np.array(X.T.dot(X), dtype=np.float64))
        temp2 = X.T.dot(A)
        ols = temp1.dot(temp2)
    except np.linalg.LinAlgError:
        ols = [np.inf for i in range(len(theta))]

    return(ols)


def run_model(data_init, country, times, I, x_, W, territories, constant, palette, title, save, path = "", data_hat = None, train_test = False, test_size = 3, ref_time = 2013):
    country_name = country
    country = pycountry.countries.get(name=country_name).alpha_3
    y = data_init
    y_ = y.rename(columns = {country: "Value"})
    y_ = y_["Value"]
    y_ = y_.reset_index(level=['Province', 'Year'])
    #x_["y_prev_2"] = np.log(pd.DataFrame(data_init.shift().loc[(slice(None), slice(None)), country]))
    data_init = bdf.filter_origin_country_dataset(data_init, country, times, x_.index.levels[0].tolist(), x_, prev = 1)

    data_all = data_init.copy()
    data_all.index = data_all.index.swaplevel(0, 1)
    data_all.sort_index(inplace=True)
    data_ = data_all[["y_prev_1", "y"]]

    if type(data_hat) != type(None):
        data_hat = bdf.filter_origin_country_dataset(data_hat, country, times, x_.index.levels[0].tolist(), x_, prev = 1)
        data_hat.index = data_hat.index.swaplevel(0, 1)
        data_hat.sort_index(inplace=True)
        data_hat = data_hat[["y_prev_1", "y"]]

    print("---------- Step I ----------")
    initial_time = datetime.datetime.now()
    print ("Current time: " + str(initial_time.strftime('%H:%M:%S') ))

    # I-1 locations + beta + ro
    random.seed(123)
    param_init = [0 for i in range(len(territories)+1)]

    if train_test:
        res_stepI =  minimize(stepI, param_init, args = (data_, W, times[:-test_size], I, territories, data_hat), method='CG')
    else:
        res_stepI =  minimize(stepI, param_init, args = (data_, W, times, I, territories, data_hat), method='CG')

    print(res_stepI.message)

    final_time = datetime.datetime.now()
    print ("Current time: " + str(final_time.strftime('%H:%M:%S')))
    print("Computational time: " + str((final_time - initial_time)))

    # Step I results and validation
    beta_hat = res_stepI.x[0]
    a_hat = res_stepI.x[1:-1]
    rho_hat = res_stepI.x[-1]

    terr_not_ref = [i for i in territories if i != I]

    idx = pd.MultiIndex.from_product([times, terr_not_ref], names=['Year', 'Province'])

    #col = ['Immigrant Stock', 'Prediction step I', 'MI 3 selection','MI 5 selection','MI 7 selection', 'MI 10 selection', 'MI 15 selection', 'MI 20 selection']
    #ks = [3, 5, 7, 10, 15, 20]
    col = ['Immigrant Stock', 'Prediction step I', '1 features', '2 features',
           '3 features', '4 features',  '5 features', '6 features', '7 features']
    ks = [1, 2, 3, 4, 5, 6, 7]
    df = pd.DataFrame('-', idx, col)
    

    for t in times[:]:
        df.loc[(t, slice(None)), 'Immigrant Stock'] = data_.loc[(t, terr_not_ref), "y"].values
        if type(data_hat) != type(None):
            df.loc[(t, slice(None)), 'Prediction step I'] = np.exp(beta_hat*np.log((data_.loc[(t, terr_not_ref), "y_prev_1"]/data_.loc[(t, I), "y_prev_1"]).values) + a_hat + np.log([data_hat.loc[(t, I), "y"] for i in terr_not_ref]))
        else:
            df.loc[(t, slice(None)), 'Prediction step I'] = np.exp(beta_hat*np.log((data_.loc[(t, terr_not_ref), "y_prev_1"]/data_.loc[(t, I), "y_prev_1"]).values) + a_hat + np.log([data_.loc[(t, I), "y"] for i in terr_not_ref]))


    print("---------- Step II ----------")
    thetas_hat = {}
    cs_hat = {}
    final_hat = pd.DataFrame(columns = col[2:])

    for k, col_name in zip(ks, col[2:]):
        print("---------- %f ----------" %k)
        print("Current time: " + str(datetime.datetime.now().strftime('%H:%M:%S')))
        '''var_k_combinations = [x for x in itertools.combinations(x_.columns, k)]
        df_temp = pd.DataFrame('-', idx, var_k_combinations)'''
       # All combinations
        if k == ks[0]:
            var_k_combinations = [
                x for x in itertools.combinations(x_.columns, k)]
        # The best combination of k-1 + each new features -> otherwise too slow and memory error
        else:
            var_k_combinations = [
                x for x in itertools.combinations(x_.columns, k)]
            var_k_combinations = [
                x for x in var_k_combinations if set(best_k).issubset(x)]

        df_temp = pd.DataFrame('-', idx, var_k_combinations)

        for t in times[:]:
            df_temp.loc[(t, slice(None)), 'Immigrant Stock'] = data_.loc[(t, terr_not_ref), "y"].values

        R2_temp = {}
        R2_adj_temp = {}

        for var in var_k_combinations:
            #print(var)
            xs_ = data_all.loc[ref_time, var]

            random.seed(123)
            if constant:
                param_init = [0 for i in range(len(xs_.columns)+1)]
                #res_stepII =  minimize(stepII_constant, param_init, args = (a_hat, xs_, I, territories), method='CG')
                '''res_stepII =  minimize(stepII_constant, param_init,
                                    args = (data_, W, times, beta_hat, rho_hat, xs_, I, territories, data_hat), method='CG')'''
            else:
                param_init = [0 for i in range(len(xs_.columns))]
                #res_stepII =  minimize(stepII, param_init, args = (a_hat, xs_, I, territories), method='CG')
                '''res_stepII =  minimize(stepII, param_init,
                                    args = (data_, W, times, beta_hat, rho_hat, xs_, I, territories, data_hat), method='CG')'''
            res_stepII =  stepII(param_init, a_hat, xs_, I, territories, constant)

            x_I = xs_.loc[I].values

            if constant:
                c_hat = res_stepII[-1]
                theta_hat = res_stepII[:-1]
            else:
                c_hat = 0
                theta_hat = res_stepII

            cs_hat[var] = c_hat
            thetas_hat[var] = theta_hat
                

            fixed_hat = [np.dot(np.subtract(xs_.loc[i].values, x_I), theta_hat) + c_hat for i in terr_not_ref]

            for t in times[:]:
                if type(data_hat) != type(None):
                    df_temp.loc[(t, slice(None)), var] = np.exp(beta_hat*np.log((data_.loc[(t, terr_not_ref), 
                    "y_prev_1"]/data_.loc[(t, I), "y_prev_1"]).values) + fixed_hat + np.log([data_hat.loc[(t, I), "y"] 
                    for i in terr_not_ref]))
                else:
                    df_temp.loc[(t, slice(None)), var] = np.exp(beta_hat*np.log((data_.loc[(t, terr_not_ref), 
                    "y_prev_1"]/data_.loc[(t, I), "y_prev_1"]).values) + fixed_hat + np.log([data_.loc[(t, I), "y"] 
                    for i in terr_not_ref]))

           
        #for c in df_temp.columns.tolist()[1:]:
            # Validation: between all the combination of k vars, return the best one (in terms of R2)
            if train_test:
                R2_temp[var] = 1 - (sum(np.subtract(df_temp.loc[(times[-test_size:], slice(None)), "Immigrant Stock"].values,
                                                    df_temp.loc[(times[-test_size:], slice(None))][var].values)**2) / sum((df_temp.loc[(times[-test_size:], slice(None)), "Immigrant Stock"].values)**2))
                # k: number of independet vars
                # len(df) includes also the reference territory
                n = len(times[-test_size:])*len(territories)
                R2_adj_temp[var] = 1 - (1 - R2_temp[var])*((n - 1)/(n - k - 1))
            else:
                R2_temp[var] = 1 - (sum(np.subtract(df_temp["Immigrant Stock"].values,
                                                    df_temp[var].values)**2) / sum((df_temp["Immigrant Stock"].values)**2))
                n = len(times)*len(territories)
                R2_adj_temp[var] = 1 - (1 - R2_temp[var])*((n - 1)/(n - k - 1))
        
        best_k = max(R2_adj_temp, key=lambda k: R2_adj_temp[k])
        df.loc[(slice(None), slice(None)), '%s features' % str(k)] = df_temp.loc[(
            slice(None), slice(None))][best_k]
    
        final_hat.loc["R2", '%s features' %
                      str(k)] = round(R2_temp[best_k], 5)
        final_hat.loc["R2_adj", '%s features' %
                      str(k)] = round(R2_adj_temp[best_k], 5)

        for best_k_single, v_best in zip(best_k, thetas_hat[best_k]):
            final_hat.loc[best_k_single, '%s features' %
                          str(k)] = v_best
        if constant:
            final_hat.loc['constant', '%s features' %
                          str(k)] = cs_hat[best_k]
    if len(terr_not_ref) <= 2:
        plt_seed = 121
    else:
        if len(terr_not_ref) <= 4:
            plt_seed = 221
        else:
            plt_seed = 231

    title = "Immigrant Stock VS "+title+" "+country_name
    #relation_plot_time_variant_intern_function(df, terr_not_ref, times, df.columns.tolist(), plt.figure(1, figsize=(15,10)), plt_seed, 45, palette, None, title, save, path = "")
    pdf.relation_plot_time_variant(df, df.columns.tolist()[
                                   1:], y_, terr_not_ref, 45, title, palette, save, path, sub_iteration=False, double_scale_x=False)

    sns.set_style("whitegrid")
    fig = plt.figure(1, figsize=(15, 10))
    plt_seed = 121
    rot = 30
    ax = fig.add_subplot(plt_seed)
    ax = sns.pointplot(
        y=final_hat.loc['R2'].values, x=final_hat.loc['R2'].index)
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    sns.despine(ax=ax, right=True, left=True)
    ax.set_xlabel("")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=rot)
    plt.title("R2 as the number of features increases", fontsize=14)

    plt_seed += 1
    ax = fig.add_subplot(plt_seed)
    ax = sns.pointplot(y=final_hat.loc['R2_adj'].values,
                       x=final_hat.loc['R2_adj'].index)
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    sns.despine(ax=ax, right=True, left=True)
    ax.set_xlabel("")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=rot)
    plt.title("Adjusted R2 as the number of features increases", fontsize=14)

    if save == False:
        plt.show()
    else:
        path_temp = path.split("/")[:-1]
        path_temp.extend(["R2_trend_" + path.split("/")[-1]+".png"])
        plt.savefig("/".join(path_temp), bbox_inches='tight')
    plt.close()

    est_param = ["beta", "a_Centro", "a_Isole",
                 "a_Nord Est", "a_ Nord Ovest", "a_Sud", "rho"]
    res_params = [y for x in [[beta_hat], a_hat, [rho_hat]] for y in x]
    res_params_ = pd.DataFrame(index=est_param, columns=["Values"])

    for i, j in zip(res_params, est_param):
        res_params_.loc[j, "Values"] = i

    return(df, final_hat, res_params_)
