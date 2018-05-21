#%%
import matplotlib.pyplot as plt
list1 = [3,4,5,6,9,12]
list2 = [8,12,14,15,17,20]
fig = plt.figure(figsize=(4,3))
ax = fig.add_subplot(111)
ax.plot(list1, list2)
fig.savefig('fig2.png', dpi = 500)
plt.close()