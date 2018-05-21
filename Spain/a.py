#%%
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('iris')

# plot
f, axes = plt.subplots(4, 4, figsize=(10, 10), sharex=True)
sns.distplot(df["sepal_length"], color="skyblue", ax=axes[0, 0])
sns.distplot(df["sepal_width"], color="olive", ax=axes[0, 1])
sns.distplot(df["petal_length"], color="gold", ax=axes[1, 0])
sns.distplot(df["petal_width"], color="teal", ax=axes[1, 1])
sns.distplot(df["sepal_length"], color="skyblue", ax=axes[0, 2])
sns.distplot(df["sepal_width"], color="olive", ax=axes[0, 3])
sns.distplot(df["petal_length"], color="gold", ax=axes[1, 2])
sns.distplot(df["petal_width"], color="teal", ax=axes[1, 3])
sns.distplot(df["sepal_length"], color="skyblue", ax=axes[2, 0])
sns.distplot(df["sepal_width"], color="olive", ax=axes[2, 1])
sns.distplot(df["petal_length"], color="gold", ax=axes[3, 0])
sns.distplot(df["petal_width"], color="teal", ax=axes[3, 1])
sns.distplot(df["sepal_length"], color="skyblue", ax=axes[2, 2])
sns.distplot(df["sepal_width"], color="olive", ax=axes[2, 3])
sns.distplot(df["petal_length"], color="gold", ax=axes[3, 2])
sns.distplot(df["petal_width"], color="teal", ax=axes[3, 3])


plt.show()

#%%
sns.set_style("whitegrid")
fig = plt.figure(1, figsize=(15, 10))
plt_seed = 51
for i in range(1, 20):
    ax = fig.add_subplot(5, 4, i)
    #print(plt_seed)
    ax = sns.distplot(df["sepal_length"], color="skyblue")
    #print(plt_seed)
    plt_seed += 1
plt.show()
plt.close()
