import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import seaborn as sns
import palettable#python颜色库
m = []
for i in range(18):
    m.append(map(float,input().split()))
mm = DataFrame(m)
plt.figure(figsize=(14, 10))
sns.heatmap(data=mm, cmap='YlGnBu', annot_kws={"fontsize":0})
plt.title('Alejandro Davidovich Fokina')
plt.savefig('iii.png')
plt.show()