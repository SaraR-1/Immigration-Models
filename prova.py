#%%
import pandas as pd

#%%
a = pd.read_table("Paper_2005_2016/spatial_autocorr_model_est_params1_romania.csv", sep = "\t")
a = a.round(4)

for i in a.index:
    print("| %s | %f |" % (a.loc[i]["Unnamed: 0"], a.loc[i]["Values"]))
