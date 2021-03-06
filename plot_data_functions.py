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
        plt.savefig(path+".png",  box_extra_artists=(lgd,),
                    bbox_inches='tight', dpi=300)
    plt.close()

def relation_plot_time_variant_intern_function(data_, temp_territories, time_idx, cols, y, fig, plt_seed, rot, palette, info, title, save, path = "", double_scale_x = True):
    x = 1
    for r in temp_territories:
        if plt_seed == 451:
            plt.rc('font', size=7)
            scale = .5
            lgd_size = 9
        else:
            plt.rc('font', size=10)
            scale = .8
            lgd_size = 12
        y_i = [y.get_group((r, t))["Value"].sum() for t in time_idx]
        y_i_mean = np.mean(y_i)

        sns.set_style("whitegrid")

        ax = fig.add_subplot(int(str(plt_seed)[0]), int(str(plt_seed)[1]), x)
        ax.tick_params(axis='x', which='minor', labelsize='small', rotation=rot)
        legend = []
        ax = sns.pointplot(y=y_i, x=time_idx, scale=scale)
        legend.append(mlines.Line2D([], [], markersize=15, label="Immigrant Stock"))
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        sns.set_style("white")
        if double_scale_x:
            ax2 = ax.twinx()
            for c in cols:
                x_i = [data_.loc[t].loc[r][c] for t in time_idx]
                # Color - always +1 because the first color is for the real value (ax)
                ax2 = sns.pointplot(y = x_i, x = time_idx, color = palette[cols.index(c)+1])
                legend.append(mlines.Line2D([], [], markersize=15, label=c.split("-")[0], color = palette[cols.index(c)+1]))

            #sns.despine(ax=ax, right=True, left=True)
            sns.despine(ax=ax2, left=True, right=False)
            #ax.set_xlabel("")
            ax2.set_xlabel("")
            ax2.spines['right'].set_color('white')
            ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        else:
            for c in cols:
                x_i = [data_.loc[t].loc[r][c] for t in time_idx]
                # Color - always +1 because the first color is for the real value (ax)
                ax2 = sns.pointplot(y=x_i, x=time_idx,
                                    color=palette[cols.index(c)+1], scale=scale)
                legend.append(mlines.Line2D([], [], markersize=15, label=c.split(
                    "-")[0], color=palette[cols.index(c)+1]))

        sns.despine(ax=ax, right=True, left=True)
        ax.set_xlabel("")
        if plt_seed != 451:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=rot)
        else:
            ax.set_xticklabels("", rotation=rot)
        #plt.title(r, fontsize = 14)
        #plt.legend(handles = legend, prop={'size':14}, loc='best')
        plt.title(r, fontsize = 14)
        #plt_seed += 1
        x += 1

    if len(temp_territories)%2 == 0:
        lgd = plt.legend(handles=legend, loc='center left', bbox_to_anchor=(
            1.05, 0.05+int(str(plt_seed)[0])), fancybox=True, fontsize=lgd_size)
    else:
        lgd = plt.legend(handles=legend, loc='center left', bbox_to_anchor=(
            2.35, 0.05+int(str(plt_seed)[0])), fancybox=True, fontsize=lgd_size)

    if len(temp_territories) == 2:
        lgd = plt.legend(handles=legend, loc='center left',
                         bbox_to_anchor=(1.05, .925), fancybox=True, fontsize=lgd_size)

    if len(temp_territories) == 9:
        lgd = plt.legend(handles=legend, loc='center left',
                         bbox_to_anchor=(1.1, 3.25), fancybox=True, fontsize=lgd_size)
        
    if plt_seed == 451:
            title = title + \
                " - years %s - %s" % (str(time_idx[0]), str(time_idx[-1]))
    else: 
        pass  

    fig.suptitle(title, fontsize = 14)
    if save == False:
        plt.show()
    else:
        plt.savefig(path+".png", box_extra_artists=(lgd,), bbox_inches='tight', dpi=300)
    plt.close()

    return(info)


def relation_plot_time_variant(data_, cols, y, zones_data, rot, title, palette, save, path="", sub_iteration=True, double_scale_x=True, title_add=" in Italian Zones"):
    if type(zones_data) != list:
        territories = list(set(zones_data["Zona"]))
    else:
        territories = zones_data
    y_grouped = y.groupby(["Province", "Year"])
    time_idx = data_.index.levels[0]

    fig = plt.figure(1, figsize=(15,10))

    info = {c: {"R2": [], "MSE": [], "Pearson": [], "Spearman": [], "Kendall": []} for c in cols}
    if len(territories) <= 2:
        plt_seed = 121
    else:
        if len(territories) <= 4:
            plt_seed = 221
        else:
            plt_seed = 231
    if len(territories) == 19:
        plt_seed = 451
    info = relation_plot_time_variant_intern_function(data_, territories, time_idx, cols, y_grouped, fig, plt_seed, rot, palette, info, "Immigrant Stock VS "+title+title_add, save, path+"zones", double_scale_x = double_scale_x)

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
