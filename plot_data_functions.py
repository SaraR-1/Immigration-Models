import pandas as pd
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import scipy

def relation_plot_time_invariant(data_, cols, y, rot, title, save, path):
    fig = plt.figure(1, figsize=(15,8))

    plt_seed = 111
    for c in cols:
        sns.set_style("whitegrid")

        ax = fig.add_subplot(plt_seed)
        ax.tick_params(axis='x', which='minor', labelsize='small', labelcolor='m', rotation=30)
        legend = []
        x_idx = [x.split(" / ")[0] for x in data_.index]
        ax = sns.pointplot(y = getattr(data_, y), x = x_idx)
        legend.append(mlines.Line2D([], [], markersize=15, label="Immigrant Stock"))
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        sns.set_style("white")
        ax2 = ax.twinx()

        ax2 = sns.pointplot(y = getattr(data_, c), x = x_idx, color = "red")
        legend.append(mlines.Line2D([], [], markersize=15, label=c, color = "red"))

        sns.despine(ax=ax, right=True, left=True)
        sns.despine(ax=ax2, left=True, right=False)

        ax2.spines['right'].set_color('white')
        ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

        ax.set_xticklabels(ax.get_xticklabels(), rotation=rot)
        plt.xticks(rotation=90)
        plt.xlabel("", fontsize=12)
        plt.ylabel("", fontsize=12)
        lgd = plt.legend(handles = legend, loc='upper center', bbox_to_anchor=(0.5, -0.25), fancybox=True, ncol = 2)

        plt_seed += 1

    #plt.legend(patches, labels, loc = "best", fontsize = 10, framealpha = 0.5)
    #plt.title("%s prediction - %d" %(country, k), fontsize = 16)
    fig.suptitle(title, fontsize = 14)
    if save == False:
        plt.show()
    else:
        plt.savefig(path+".png",  box_extra_artists=(lgd,), bbox_inches='tight')
    plt.close()

def relation_plot_time_variant_intern_function(data_, temp_territories, time_idx, cols, y, fig, plt_seed, rot, palette, info, title, save, path = ""):

    for r in temp_territories:
        y_i = [y.get_group((r, t))["Value"].sum() for t in time_idx]
        y_i_mean = np.mean(y_i)

        sns.set_style("whitegrid")

        ax = fig.add_subplot(plt_seed)
        ax.tick_params(axis='x', which='minor', labelsize='small', rotation=30)
        legend = []
        ax = sns.pointplot(y = y_i, x = time_idx)
        legend.append(mlines.Line2D([], [], markersize=15, label="Immigrant Stock"))
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        sns.set_style("white")
        ax2 = ax.twinx()
        for c in cols:
            x_i = [data_.loc[t].loc[r][c] for t in time_idx]
            # Color - always +1 because the first color is for the real value (ax)
            ax2 = sns.pointplot(y = x_i, x = time_idx, color = palette[cols.index(c)+1])
            legend.append(mlines.Line2D([], [], markersize=15, label=c.split("-")[0], color = palette[cols.index(c)+1]))


            #info[c]["R2"].append(1 - sum(np.subtract(y_i, x_i)**2) / sum((y_i - y_i_mean)**2))
            #print(R2)
            #info[c]["MSE"].append(sum(np.subtract(y_i, x_i)**2)/len(y_i))

            #info[c]["Pearson"].append(scipy.stats.pearsonr(y_i, x_i)[0])
            #info[c]["Spearman"].append(scipy.stats.spearmanr(y_i, x_i)[0])
            #info[c]["Kendall"].append(scipy.stats.kendalltau(y_i, x_i)[0])

            #print("------------------ %s and %s info ------------------" %(r, c))

            #print("The R2 score is: %f" %(R2))
            #print("The MSE score is: %f" %(MSE))

            #print("The Pearson's correlation coefficient is: %f, with p-value %f" %(scipy.stats.pearsonr(y_i, x_i)[0], scipy.stats.pearsonr(y_i, x_i)[1]))
            #print("The Spearman's correlation coefficient is: %f, with p-value %f" %(scipy.stats.spearmanr(y_i, x_i)[0], scipy.stats.spearmanr(y_i, x_i)[1]))
            #print("The Kendall's correlation coefficient is: %f, with p-value %f" %(scipy.stats.kendalltau(y_i, x_i)[0], scipy.stats.kendalltau(y_i, x_i)[1]))

        sns.despine(ax=ax, right=True, left=True)
        sns.despine(ax=ax2, left=True, right=False)
        ax.set_xlabel("")
        ax2.set_xlabel("")
        ax2.spines['right'].set_color('white')
        ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))


        ax.set_xticklabels(ax.get_xticklabels(), rotation=rot)
        #plt.title(r, fontsize = 14)
        #plt.legend(handles = legend, prop={'size':14}, loc='best')
        plt.title(r, fontsize = 14)
        plt_seed += 1

    if len(temp_territories)%2 == 0:
        lgd = plt.legend(handles = legend, loc='center left', bbox_to_anchor=(1.05, 0.05+int(str(plt_seed)[0])), fancybox=True)
    else:
        lgd = plt.legend(handles = legend, loc='center left', bbox_to_anchor=(2.35, 0.05+int(str(plt_seed)[0])), fancybox=True)

    if len(temp_territories) == 2:
            lgd = plt.legend(handles = legend, loc='center left', bbox_to_anchor=(1.05, .925), fancybox=True)
    fig.suptitle(title, fontsize = 14)
    if save == False:
        plt.show()
    else:
        plt.savefig(path+".png", box_extra_artists=(lgd,), bbox_inches='tight')
    plt.close()

    return(info)

def relation_plot_time_variant(data_, cols, y, zones_data, rot, title, palette, save, path = "", sub_iteration = True):
    territories = list(set(zones_data["Zona"]))
    y_grouped = y.groupby(["Province", "Year"])
    time_idx = data_.index.levels[0]

    fig = plt.figure(1, figsize=(15,10))

    info = {c: {"R2": [], "MSE": [], "Pearson": [], "Spearman": [], "Kendall": []} for c in cols}
    info = relation_plot_time_variant_intern_function(data_, territories, time_idx, cols, y_grouped, fig, 231, rot, palette, info, "Immigrant Stock VS "+title+" in Italian Zones", save, path+"zones")

    '''for c in cols:
        print("----------- %s - zones mean -----------" %(c))
        for k in info[c].keys():
            if k != "R2" and k != "MSE":
                print("The %s's correlation coefficient is: %f" %(k, np.mean(info[c][k])))
            else:
                print("The %s is: %f" %(k, np.mean(info[c][k])))
'''
    #info = {c: {"R2": [], "MSE": [], "Pearson": [], "Spearman": [], "Kendall": []} for c in cols}
    if sub_iteration:
        # A single figure with 21+legend boxes is difficult to analyse. What to do? Figure for each zone.
        grouped_zone = zones_data.groupby(["Zona"])["Regione"]
        for z in territories:
            temp_region = grouped_zone.get_group(z).values

            fig = plt.figure(1, figsize=(15,10))

            if len(temp_region) <= 2:
                plt_seed = 121
            else:
                if len(temp_region) <= 4:
                    plt_seed = 221
                else:
                    plt_seed = 231
            time_idx = data_.index.levels[0]

            # For each region in the zone, produce a plot (box) in the figure
            info = relation_plot_time_variant_intern_function(data_, temp_region, time_idx, cols, y_grouped, fig, plt_seed, rot, palette, info, "Immigrant Stock VS "+title+" in "+z, save, path+z)
    else:
        pass

'''    for c in cols:
        print("----------- %s - regions mean -----------" %(c))
        for k in info[c].keys():
            if k != "R2" and k != "MSE":
                print("The %s's correlation coefficient is: %f" %(k, np.mean(info[c][k])))
            else:
                print("The %s is: %f" %(k, np.mean(info[c][k])))'''
