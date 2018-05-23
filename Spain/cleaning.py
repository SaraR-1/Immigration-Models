#%%
import pandas as pd

years = list(range(1998, 2018))
complete = pd.DataFrame(
    columns=["Province", "Country", "Year", "Gender", "Value"])
filename = "Data/spain_foreigners_flow.tsv"
cols = ["Province"] + \
    [str(i)+"_"+j for j in ["Total", "Male", "Female"] for i in years]

skip = 8
step = 53
n_cols = len(cols)
pointer = step + skip
while pointer <= 7351:
    print(skip, pointer)
    temp = pd.read_table("Data/spain_foreigners_flow.tsv", sep="\t", skiprows=skip,
                         nrows=step, header=None, usecols=list(range(n_cols)), names=cols)
    temp.index = [i.split()[1]
                  for i in temp["Province"]]
    '''temp["Province"].replace({i: i.split()[1]
                            for i in temp["Province"]}, inplace=True)'''
    del temp["Province"]

    with open(filename, 'r') as filehandle:
        current_line = 1
        for line in filehandle:
            if current_line == skip:
                country = line.split("\t")[0].title()
                break
            current_line += 1

    for i in temp.columns:
        for j in temp.index:
            complete = complete.append({k: v for k, v in zip(complete.columns, [
                j, country, int(i.split("_")[0]), i.split("_")[1], temp.loc[j, i]])}, ignore_index=True)

    skip += step + 1
    pointer += step + 1

complete = complete.reset_index()
complete["Province"].replace(
    {"Coruña": "A Coruña", "Palmas": "Las Palmas", "Rioja": "La Rioja", "Santa": "Santa Cruz de Tenerife",
     "Asturias, Principado de": "Principado de Asturias", " País Vasco": "País Vasco",
     "Madrid, Comunidad de": "Comunidad de Madrid", "Murcia, Región de": "Región de Murcia",
     "Navarra, Comunidad Foral de": "Comunidad Foral de Navarra", "Balears,": "Illes Balears", "Ciudad": "Ciudad Real"}, inplace=True)
complete.set_index("Province", inplace=True)
complete.to_csv("Data/spain_working.tsv", sep="\t")

############################################################################################

#%%
import pandas as pd

complete = pd.read_table("Data/spain_working.tsv", sep = "\t", index_col=0)
complete.head()

aut_comm = pd.read_table("Data/provinces_auton_comm.tsv", sep = ";")
aut_comm.index = aut_comm["Province"]
del aut_comm["Province"]
aut_comm.head()

complete.replace(aut_comm.to_dict()[
    'Autonomous community'], inplace=True)
complete.head()

#%%
complete = complete[complete["Gender"] == "Total"]
complete = pd.DataFrame(complete.groupby(["Province", "Country", "Year", "Gender"])[
    "Value"].sum())
# Drop "Gender" col
complete.index = complete.index.droplevel(level=3)
complete.head()

complete.to_csv("Data/spain_working_aut_comm.tsv", sep="\t")

############################################################################################

#%%
import pandas as pd
import pycountry

complete = pd.read_table("Data/spain_working_aut_comm.tsv", sep="\t")
complete.head()

#%%
# dictionary with the structure: {country: iso3}
iso3_all_countrie_engl = {}
not_found = []
countries_list = sorted(list(set(complete["Country"])))
for i in countries_list:
    try:
        iso3_all_countrie_engl[i] = pycountry.countries.get(name=i).alpha_3
    except:
        not_found.append(i)

interest_not_found = ['Arabia Saudi', 'Bolivia', 'Bosnia And Herzegovina',  'Czech Republic',
                      'Democratic Republic Of Congo', 'Green Cape', 'Iran', 'Ivory Coast',
                      'Kazajstan', 'Kenia', 'Macedonia (Ex-Yugoslavian Republic)', 'Moldavia', 
                      'Russia', 'South Korea',  'Syria', 'The Netherlands', 'The Slovak Republic', 
                      'United States Of America', 'Venezuela', 'Vietnam']
interest_not_found_corr = ["SAU", "BOL", "BIH", "CZE", "COD", "CPV", "IRN", "CIV",
                           "KAZ", "KEN", "MKD", "MDA", "RUS", "KOR", "SYR", "NLD", "SVK",
                           "USA", "VEN", "VNM"]

for i, j in zip(interest_not_found, interest_not_found_corr):
    iso3_all_countrie_engl[i] = j

complete = complete[complete["Country"].isin(iso3_all_countrie_engl.keys())]
complete.replace(iso3_all_countrie_engl, inplace=True)
complete.to_csv("Data/spain_working_aut_comm.tsv", sep="\t")
complete.head()

############################################################################################
#%%
import pandas as pd

#xs = pd.DataFrame()
ord_list_comm = ["Andalucía", 'Aragón', 'Principado de Asturias', 'Illes Balears',
                 'Canarias', 'Cantabria', 'Castilla y León', 'Castilla - La Mancha', 'Cataluña',
                 'Comunitat Valenciana', 'Extremadura', 'Galicia', 'Comunidad de Madrid', 'Región de Murcia',
                 'Comunidad Foral de Navarra', 'País Vasco', 'La Rioja', 'Cueta', 'Melilla']

files = ["poblacion_total.csv", "tasa_bruta_mortalidad.csv", "tasa_bruta_natalidad.csv",
         "tasa_fecundidad.csv", "PIB_pc.csv"]
skip = 8

for file_name in files:
    print(file_name)
    # Read all the file, but the initial 8 lines
    temp = pd.read_table("Data/"+file_name, sep="\t", skiprows=skip, header=None, usecols=[0,1], names=["Year", file_name.split(".")[0]])

    # Select the years indexes
    col_list = list(set(temp["Year"]))
    col_list_years = []
    for i in col_list:
        try:
            a = int(i)
            temp["Year"].replace({i: a}, inplace=True)
            col_list_years.append(a)
        except ValueError:
            pass

    temp = temp[temp["Year"].isin(col_list_years)]
    temp.index = range(len(temp))
    n_years = len(col_list_years)

    temp["Province"] = [i for i in ord_list_comm for j in range(n_years)]

    temp[file_name.split(".")[0]] = temp[file_name.split(".")[0]].apply(
        lambda x: x.replace(".", ""))
    temp[file_name.split(".")[0]] = temp[file_name.split(".")[0]].apply(
        lambda x: x.replace(",", "."))
    temp[file_name.split(".")[0]] = temp[file_name.split(".")[0]].astype(float)

    temp = temp.set_index(['Year', 'Province'])
    try:
        xs = pd.concat([xs, temp], axis=1, join='inner')
    except:
        xs = temp.copy()

files = ["tasa_actividad.csv", "tasa_paro.csv", "ocupados.csv"]
for file_name in files:
    # Read all the file, but the initial 8 lines
    temp = pd.read_table("Data/"+file_name, sep="\t", skiprows=skip,
                            header=None, usecols=[0, 1], names=["Year", file_name.split(".")[0]])
    # List of refer years is know
    years = range(2002, 2018)
    # As annual value let's consider the mean of the 4 yearly values (dati trimestrali)
    col_list = list(set(temp["Year"]))
    #%%
    col_list_years = []
    for i in col_list:
        try:
            a = int(i.split("T")[0])
            temp["Year"].replace({i:a}, inplace = True)
            col_list_years.append(a)
        except ValueError:
                pass

    col_list_years = [i for i in col_list_years if i != 2018]
    temp = temp[temp["Year"].isin(col_list_years)]
    temp.index = range(len(temp))
    n_years = len(col_list_years)

    temp["Province"] = [i for i in ord_list_comm for j in range(n_years)]

    temp[file_name.split(".")[0]] = temp[file_name.split(".")[0]].apply(
        lambda x: x.replace(".", ""))
    temp[file_name.split(".")[0]] = temp[file_name.split(".")[0]].apply(
        lambda x: x.replace(",", "."))
    temp[file_name.split(".")[0]] = temp[file_name.split(".")[0]].astype(float)

    temp = temp.groupby(["Year", "Province"])[file_name.split(".")[0]].mean()

    xs = pd.concat([xs, temp], axis=1, join='inner')

#%%
xs.to_csv("Data/xs_aut_comm.tsv", sep="\t")

#%%
ord_list_comm = ["Andalucía", 'Aragón', 'Principado de Asturias', 'Illes Balears',
                 'Canarias', 'Cantabria', 'Castilla y León', 'Castilla - La Mancha', 'Cataluña',
                 'Comunitat Valenciana', 'Extremadura', 'Galicia', 'Comunidad de Madrid', 'Región de Murcia',
                 'Comunidad Foral de Navarra', 'País Vasco', 'La Rioja', 'Cueta', 'Melilla']
complete = complete[complete["Province"].isin(ord_list_comm)]
complete.to_csv("Data/spain_working_aut_comm.tsv", sep="\t")
############################################################################################
#%%
import pandas as pd
import sys
sys.path.append('/home/sara/Documents/Immigration/Shared_models')
import build_data_functions as bdf
import plot_data_functions as pdf
import model_functions as mf
import plot_model_functions as pmf
import panelOLS_models
import spatial_error_model as sem
import spatial_error_model_new as semnew


complete = pd.read_table("Data/spain_working_aut_comm.tsv", sep="\t", index_col= 0)
complete.head()
#territories = sorted(list(set(complete["Province"])))
#territories = [i for i in territories if i != "Spain"]

#%%
ord_list_comm = ["Andalucía", 'Aragón', 'Principado de Asturias', 'Illes Balears',
                 'Canarias', 'Cantabria', 'Castilla y León', 'Castilla - La Mancha', 'Cataluña',
                 'Comunitat Valenciana', 'Extremadura', 'Galicia', 'Comunidad de Madrid', 'Región de Murcia',
                 'Comunidad Foral de Navarra', 'País Vasco', 'La Rioja', 'Cueta', 'Melilla']

W = W.loc[ord_list_comm, ord_list_comm]
W = W.fillna(0)
W = W.reindex(sorted(W.columns), axis=1)
W = W.reindex(sorted(W.columns), axis=0)
W.to_csv("Data/dist_matrix.tsv", sep="\t")

#%%
complete = pd.read_table(
    "Data/spain_working_aut_comm.tsv", sep="\t", index_col=0)

complete["Province"].replace(
    {"Comunidad de Madrid": "Com. de Madrid", 'Castilla - La Mancha': 'Castilla-La Mancha', "Región de Murcia": "Reg. de Murcia",
     "Comunidad Foral de Navarra": "Com. Foral de Navarra", "Principado de Asturias": "Princ. de Asturias", 
     "Comunitat Valenciana": "Com. Valenciana"}, inplace=True)
complete.to_csv("Data/spain_working_aut_comm.tsv", sep="\t")

#%%
W = pd.read_table("Data/dist_matrix.tsv", sep="\t", index_col=0)

W = W.rename({"Comunidad de Madrid": "Com. de Madrid", 'Castilla - La Mancha': 'Castilla-La Mancha', "Región de Murcia": "Reg. de Murcia",
     "Comunidad Foral de Navarra": "Com. Foral de Navarra", "Principado de Asturias": "Princ. de Asturias",
     "Comunitat Valenciana": "Com. Valenciana"}, axis="columns")

W = W.rename({"Comunidad de Madrid": "Com. de Madrid", 'Castilla - La Mancha': 'Castilla-La Mancha', "Región de Murcia": "Reg. de Murcia",
        "Comunidad Foral de Navarra": "Com. Foral de Navarra", "Principado de Asturias": "Princ. de Asturias",
        "Comunitat Valenciana": "Com. Valenciana"}, axis="index")
W = W.reindex(sorted(W.columns), axis=1)
W = W.reindex(sorted(W.columns), axis=0)
W.to_csv("Data/dist_matrix.tsv", sep="\t")

#%%
xs = pd.read_table("Data/xs_aut_comm.tsv", sep="\t")
xs["Province"].replace(
    {"Comunidad de Madrid": "Com. de Madrid", 'Castilla - La Mancha': 'Castilla-La Mancha', "Región de Murcia": "Reg. de Murcia",
     "Comunidad Foral de Navarra": "Com. Foral de Navarra", "Principado de Asturias": "Princ. de Asturias",
     "Comunitat Valenciana": "Com. Valenciana"}, inplace=True)
xs.to_csv("Data/xs_aut_comm.tsv", sep="\t", index = False)

#%%
xs.to_csv("Data/xs_aut_comm.tsv", sep="\t", index=False)
xs

