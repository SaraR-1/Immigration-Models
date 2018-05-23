#%%
import pandas as pd
import sys
sys.path.append('/home/sara/Documents/Immigration/Shared_models')
import build_data_functions as bdf
import pycountry

complete = pd.read_table("Data/spain_working_aut_comm.tsv", sep="\t", index_col = 0)
y = bdf.pivot(complete, "Country", "Value")
# Sort the Province col by alphabetic order
y = y.sortlevel()
#y.head()
comunidades = y.index.levels[0].tolist()

for t in y.index.levels[1]:
    y.loc[("Spain", t), :] = y.loc[(comunidades, t), :].sum()
#%%
xs_zones = pd.read_table("Data/xs_aut_comm.tsv", sep="\t",
                         index_col=["Province", "Year"])

#%%
xs_zones

#%%
a = y.loc[("Spain", list(range(2002, 2017))), ].sum()
aa = list(a.nlargest(20).index)
b = [pycountry.countries.get(
    alpha_3=country).name for country in aa]
b

'''#%%
print("---------------------------------------------------------------------------")
#%%
y = pd.read_table(
    "/home/sara/Documents/Immigration/Shared_models/Data/resident_foreigners_norm.csv", sep="\t", index_col=0)
y = y.groupby(["Province", "Country", "Year"], as_index=False)["Value"].sum()
y = bdf.pivot(y, "Country", "Value")

# To get the Italy info we need to sum the 5 Italian zones
zones = list(pd.read_table("/home/sara/Documents/Immigration/Shared_models/Data/x_zones.csv",
                           sep="\t", index_col=["Province", "Year"]).index.levels[0])

for t in y.index.levels[1]:
    y.loc[("Italia", t), :] = y.loc[(zones, t), :].sum()

a = y.loc[("Italia", list(range(2003, 2017))), ].sum()
aa = list(a.nlargest(20).index)
d = [pycountry.countries.get(
    alpha_3=country).name for country in aa]
d
'''
#%%
print("---------------------------------------------------------------------------")
sorted(list(set(b).intersection(d)))
#%%
y.loc[(slice(None), list(range(2003, 2017))), "ECU"]

#%%
c.loc[(slice(None), list(range(2003, 2017))), "DEU"].sum()/2

#%%
c.loc[(slice(None), list(range(2003, 2017))), "FRA"].sum()/2


#%%
y.loc[("Cueta", list(range(2002, 2017))), ]

#%%
y.loc[(slice(None), list(range(2002, 2017))), "POL"].sum()/2

#%%
y.loc[(slice(None), list(range(2002, 2017))), "DEU"].sum()/2

#%%
y.loc[(slice(None), list(range(2002, 2017))), "FRA"].sum()/2

#%%
pycountry.countries.get(
    name="France").alpha_3


#%%
countries_list = ['China', 'Colombia', 'Ecuador', 'Germany', 'Morocco', 'Romania']
sorted(countries_list)

#%%
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
palette = ['blue', 'darkgreen', 'yellowgreen', 'orange', 'lightcoral',
           'red', 'paleturquoise', 'deepskyblue', 'mediumpurple', 'fuchsia']
sns.palplot(palette)
plt.show()
