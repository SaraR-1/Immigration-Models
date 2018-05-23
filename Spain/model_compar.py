#%%
import glob
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

all_path = ["ES_2003_2016/", "Regression_2003_2016/", "Paper_2003_2016/"]
metrics = ["MAE", "MSE", "RMSE"]
countries_list = ['Germany', 'Morocco', 'Peru', 'Poland', 'Romania']

directory = "/home/sara/Documents/Immigration/Shared_models/Spain/Model_compar"
if not os.path.exists(directory):
    os.makedirs(directory)

for c in countries_list:
    fig = plt.figure(1, figsize=(15, 10))
    plt_seed = 131
    for m in metrics:
        temp = pd.read_table(all_path[1]+'param_%s.tsv' %
                             c.lower(), sep="\t", index_col=0)
        temp = temp.loc[m]
        temp = temp.rename({i: "Regression "+i for i in temp.index})

        temp1 = pd.read_table(
            all_path[2]+'spatial_autocorr_model_est_params2_%s.tsv' % c.lower(), sep="\t", index_col=0)

        temp1 = temp1.loc[m]
        temp1 = temp1.rename({i: "Paper "+i for i in temp1.index})

        temp2_ = pd.read_table(
            all_path[0]+'ES_metrics.tsv', sep="\t", index_col=0)
        temp2 = temp2_.loc[c][m:m+".3"]
        temp2 = temp2.rename(
            {j: "ES "+str(i) for i, j in zip(list(set(temp2_.loc["Alpha"].values)), temp2.index)})

        complete = pd.concat([temp, temp1, temp2])

        sns.set_style("whitegrid")
        ax = fig.add_subplot(plt_seed)
        ax.tick_params(axis='x', which='minor',
                       labelsize='small', labelcolor='m', rotation=30)

        ax = sns.pointplot(y=complete.values, x=complete.index)
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        sns.set_style("white")
        sns.despine(ax=ax, right=True, left=True)

        plt.xticks(rotation=90)
        plt.xlabel("", fontsize=12)
        plt.ylabel("", fontsize=12)

        plt.title("Model's "+m+" " + c)

        plt_seed += 1

    plt.savefig("%s/models_mae_mse_rmse_%s.png" %
                (directory, c.lower()),  bbox_inches='tight')
    plt.close()
