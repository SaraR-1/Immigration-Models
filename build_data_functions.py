import pandas as pd
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def replace_in_list(list_, olds_, news_):
    for old_, new_ in zip(olds_, news_):
        list_[list_.index(old_)] = new_
    return(list_)

def add_row(df, rows):
    ind = range(len(df), len(df)+len(rows))
    for row, i in zip(rows, ind):
        df.loc[i] = row
    return(df)

def drop_useless(data):
    for c in data.columns:
        if len(list(set(data[c]))) == 1:
            print(c, set(data[c]))
            del data[c]

def divide_table(data, attribute):
    res = [x for _, x in data.groupby(data[attribute])]
    for r in res:
        del r[attribute]
    return res

def filtering(data, attribute, list_values):
    return data[data[attribute].isin(list_values)]

def pivot(data, attibute = None, value = None):
    idx = data.columns[(data.columns != attibute) & (data.columns != value)]
    return pd.pivot_table(data, columns=attibute, values = value, index = list(idx))

def re_ordering_df(data):
    return data.reindex(sorted(data.columns), axis=1)

def check_missing(data):
    for c in data.columns:
        if data[c].isnull().sum() != 0:
            print(c)

# del a column if more than 1/3 of its values are missing
def del_missing(data):
    threshold = 1/3*len(data)
    for c in data.columns:
        if data[c].isnull().sum() >= threshold:
            print(c)
            del data[c]

def differentiate_values(data, attribute, to_modify):
    data[to_modify] = [data[to_modify][i] + " - " + data[attribute][i] for i in data.index]
    del data[attribute]
    return data


def check_missing_index(data, time, place):
    y = data.index.levels[0]
    #p = data.index.levels[1]

    if len(y) != len(time):
        print([i for i in time if i not in y])
    sub_index_miss = set()
    for i in y:
        temp = data.loc[i].index
        if len(temp) != len(place):
            sub_index_miss.update([p for p in place if p not in temp])
    print(list(sub_index_miss))
'''    if len(p) != len(place):
        print([i for i in place if i not in p])'''

def merge_xs(features, territories):
    x = features[0].loc[(slice(None), territories), :].copy()
    for f in features[1:]:
        if set(territories).issubset(f.index.levels[1]):
            temp = f.loc[(slice(None), territories), :].copy()
            x = pd.concat([temp, x], axis = 1)
        else:
            pass

    x.index = x.index.swaplevel(0, 1)
    x.sort_index(inplace=True)

    '''    #pop = resident_norm.copy()
    idx = pop.columns[(pop.columns != "Gender") & (pop.columns != "Value")].tolist()
    pop = pop.groupby(idx, as_index=False)["Value"].sum()
    pop = pivot(pop, value = "Value")
    pop.columns = ["Population"]
    pop = pop.loc[(territories, list(range(2005, 2016))), :].copy()

    x = pd.concat([pop, x], axis = 1)'''

    return x

def fill_aggragating(to_fill, to_fill_attr, to_aggr_attr1, to_aggr_attr2, aggregation_data, data_):
    grouped = aggregation_data.groupby([to_fill_attr])
    for r in to_fill:
        list_temp = grouped.get_group(r)[to_aggr_attr1].values
        idx = data_.columns[(data_.columns != to_aggr_attr2) & (data_.columns != "Value")].tolist()
        res_temp = data_[(data_[to_aggr_attr2].isin(list_temp))].groupby(idx)["Value"].sum()
        temp = pd.DataFrame(res_temp)
        temp = temp.reset_index(level=idx)
        temp[to_aggr_attr2] = [r for i in range(len(temp))]
        temp = temp[temp.columns.tolist()[-1:] + temp.columns.tolist()[:-1]]

        data_ = pd.concat([data_, temp])

    data_.index = list(range(len(data_)))
    return data_

def filter_origin_country_dataset(data_, country, years, territories, x, prev):
    y = data_.loc[(territories, ), :][country]
    y = pd.DataFrame(y)

    y_ = y.loc[(slice(None), ), :]
    y_.columns = ["y"]

    res = pd.concat([y_, x], axis = 1)

    for p in range(1, prev+1):
        y_prev = y.copy()
        y_prev = y_prev.groupby(level=0)[country].shift(p)
        y_prev = pd.DataFrame(y_prev)

        y_prev = y_prev.loc[(slice(None), ), :]
        y_prev.columns = ["y_prev_"+str(p)]

        res = pd.concat([y_prev, res], axis = 1)

    res = res.loc[(slice(None), years), :]
    return(res)
