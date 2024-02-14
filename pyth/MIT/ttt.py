import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import seaborn as sns
import palettable#python颜色库
import random
import scipy
m = []
for i in range(300):
    p = random.random()*14-7
    for j in range(10+int(random.random()*5-2.5)):
        m.append(p)

y_smooth = scipy.signal.savgol_filter([0]+ m,53,3)  
plt.plot(+ y_smooth[:300])
print(i for i in [1,2])