#%%
import pandas as pd

#%% 
a = pd.read_table(
    "SMA_2005_2016/SMA_metrics.csv", sep="\t")

a
for i in a.index:
    print("| %s | %f |  %f |  %f |" %
          (a.loc[i]["Unnamed: 0"], a.loc[i]["MAE"], a.loc[i]["MPE"], a.loc[i]["MAPE"]))


#%%
a = pd.read_table(
    "ES_2005_2016/ES_metrics.csv", sep="\t")
a = a.round(4)
for i in a.index[1:]:
    print(" <tr>")
    for j in a.columns:
        print(" <td > %s </td>" %str(a.loc[i][j]))
    print(" <tr>")


#%%
b = ["![](https://latex.codecogs.com/gif.latex?% 5Cbeta)" , 
"![](https://latex.codecogs.com/gif.latex?a_%7BCentro%7D)", 
"![](https://latex.codecogs.com/gif.latex?a_%7BIsole%7D)", 
"![](https://latex.codecogs.com/gif.latex?a_%7BNord%20%5C%20est%7D)", 
"![](https://latex.codecogs.com/gif.latex?a_%7BNord%20%5C%20ovest%7D)", 
"![](https://latex.codecogs.com/gif.latex?a_%7BSud%7D)", 
"![](https://latex.codecogs.com/gif.latex?% 5Crho)"]
a = pd.read_table("Paper_2005_2016/spatial_autocorr_model_est_params1_albania.tsv", sep = "\t")
a = a.round(4)

for i, j in zip(a.index, b):
    print("| %s | %f |" %(j, a.loc[i]["Values"]))

#%%
a = pd.read_table(
    "Paper_2005_2016/spatial_autocorr_model_est_params2_philippines.tsv", sep="\t")
a = a.round(4)
a.columns

for i in a.index:
    print("| %s | %f |  %f |  %f |  %f |  %f |  %f |  %f | %f |" %
          (a.loc[i]["Unnamed: 0"], a.loc[i]["Entity Effect"], a.loc[i]["1 features"], a.loc[i]["2 features"], a.loc[i]["3 features"],
          a.loc[i]["4 features"], a.loc[i]["5 features"], a.loc[i]["6 features"], a.loc[i]["7 features"]))



#%%%
countries_list = ["Romania", "Morocco", "Albania", "Tunisia",
                  "Egypt", "Ecuador", "Peru", "China", "Philippines"]

for c in countries_list:
    print("![](https: // github.com/SaraR-1/Immigration-Models/blob/master/ES_2005_2016/ES_%s_zones.png)" %c.lower())


#%%
ks = [3, 5, 6]
a = ["%s features" %str(i) for i in ks]
print(a)
col = ['Immigrant Stock', 'Provious Time', 'Provious 2 Times']
col = col + a
print(col)


#%%
a = pd.read_table(
    "Regression_2006_2016/param_philippines.tsv", sep="\t")
a = a.round(4)
a.columns

for i in a.index:
    print("| %s | %f |  %f |  %f |  %f |  %f |  %f |  %f | %f |" %
          (a.loc[i]["Unnamed: 0"], a.loc[i]["Previous time"], a.loc[i]["Previous two times"], 
           a.loc[i]["Manual Selection"], a.loc[i]["MI 3 selection"], a.loc[i]["MI 5 selection"], 
           a.loc[i]["MI 7 selection"], a.loc[i]["MI 10 selection"], a.loc[i]["MI 15 selection"]))
