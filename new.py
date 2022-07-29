import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
sns.set_theme()

uniform_data = np.random.rand(10, 12)

ax = sns.heatmap(uniform_data, linewidths=.5)

plt.show()