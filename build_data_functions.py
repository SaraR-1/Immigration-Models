
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


# In[ ]:


def replace_in_list(list_, olds_, news_):
    for old_, new_ in zip(olds_, news_):
        list_[list_.index(old_)] = new_
    return(list_)


# In[ ]:


def add_row(df, rows):
    ind = range(len(df), len(df)+len(rows))
    for row, i in zip(rows, ind):
        df.loc[i] = row
    return(df)


# In[ ]:


def drop_useless(data):
    for c in data.columns:
        if len(list(set(data[c]))) == 1:
            print(c, set(data[c]))
            del data[c]


# In[ ]:


def divide_table(data, attribute):
    res = [x for _, x in data.groupby(data[attribute])]
    for r in res:
        del r[attribute]
    return res


# In[ ]:


def filtering(data, attribute, list_values):
    return data[data[attribute].isin(list_values)]


# In[ ]:


def pivot(data, attibute, value):
    idx = data.columns[(data.columns != attibute) & (data.columns != value)]
    return pd.pivot_table(data, columns=attibute, values = value, index = list(idx)) 


# In[ ]:


def re_ordering_df(data):
    return data.reindex_axis(sorted(data.columns), axis=1)


# In[ ]:


def check_missing(data):
    for c in data.columns:
        if data[c].isnull().sum() != 0:
            print(c)


# In[ ]:


# del a column if more than 1/3 of its values are missing
def del_missing(data):
    threshold = 1/3*len(data)
    for c in data.columns:
        if data[c].isnull().sum() >= threshold:
            print(c)
            del data[c]


# In[ ]:


def differentiate_values(data, attribute, to_modify):
    data[to_modify] = [data[to_modify][i] + " - " + data[attribute][i] for i in data.index]
    del data[attribute]
    return data


# In[ ]:


def check_missing_index(data, time, place):
    y = data.index.levels[0]
    p = data.index.levels[1]
    
    if len(y) != len(time):
        print([i for i in time if i not in y])
    if len(p) != len(place):
        print([i for i in place if i not in p])


# In[ ]:


def relation_plot_time_invariant(data_, cols, y, rot):    
    fig = plt.figure(1, figsize=(15,15))

    plt_seed = 221
    for c in cols:
        sns.set_style("whitegrid")

        ax = fig.add_subplot(plt_seed)
        ax.tick_params(axis='x', which='minor', labelsize='small', labelcolor='m', rotation=30)
        legend = []
        ax = sns.pointplot(y = data_[y], x = data_.index)
        legend.append(mlines.Line2D([], [], markersize=15, label="Real"))

        sns.set_style("white")
        ax2 = ax.twinx()
        ax2 = sns.pointplot(y = getattr(data_, c), x = data_.index, color = "red")
        legend.append(mlines.Line2D([], [], markersize=15, label=c, color = "red"))

        sns.despine(ax=ax, right=True, left=True)
        sns.despine(ax=ax2, left=True, right=False)

        ax2.spines['right'].set_color('white')
        
        ax.set_xticklabels(ax.get_xticklabels(), rotation=rot)
        plt.xticks(rotation=90)
        plt.xlabel("", fontsize=12)
        plt.ylabel("", fontsize=12)
        plt.legend(handles = legend, prop={'size':14}, loc='best')
        #plt.title("Real Immigrant stock VS %s" %c, fontsize = 14)

        plt_seed += 1

    #plt.legend(patches, labels, loc = "best", fontsize = 10, framealpha = 0.5)
    #plt.title("%s prediction - %d" %(country, k), fontsize = 16)
    plt.show()

