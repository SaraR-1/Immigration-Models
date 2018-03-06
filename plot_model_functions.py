import pandas as pd
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def plot_real_VS_prediction(y, xs, time_idx, country, rot, title, save, path):

    fig = plt.figure(1, figsize=(15,10))
    plt_seed = 231

    for r in xs.index.levels[0].tolist():
        y_i = y.loc[(r, years), :][country].values

        sns.set_style("whitegrid")

        ax = fig.add_subplot(plt_seed)
        ax.tick_params(axis='x', which='minor', labelsize='small', rotation=30)
        legend = []
        ax = sns.pointplot(y = y_i, x = time_idx)
        legend.append(mlines.Line2D([], [], markersize=15, label="Immigrant Stock"))

        ax = sns.pointplot(y = res.fitted_values.loc[r].fitted_values.values, x = time_idx, color = "red")
        legend.append(mlines.Line2D([], [], markersize=15, label="Immigrant Stock Prediction", color = "red"))
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))


        sns.despine(ax=ax, right=True, left=True)
        #sns.despine(ax=ax2, left=True, right=False)
        ax.set_xlabel("")
        #ax2.set_xlabel("")
        #ax2.spines['right'].set_color('white')
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))


        ax.set_xticklabels(ax.get_xticklabels(), rotation=rot)
        #plt.title(r, fontsize = 14)
        #plt.legend(handles = legend, prop={'size':14}, loc='best')
        plt.title(r, fontsize = 14)

        plt_seed += 1

    lgd = plt.legend(handles = legend, loc='upper center', bbox_to_anchor=(0.5, -.25), fancybox=True, ncol = 2)

    fig.suptitle(title, fontsize = 14)
    if save == False:
        plt.show()
    else:
        plt.savefig(path+".png",  box_extra_artists=(lgd,), bbox_inches='tight')
    plt.close()
