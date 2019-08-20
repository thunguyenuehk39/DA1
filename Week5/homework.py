import math
import numpy as np
import scipy.stats
import scipy as sp
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp

from IPython import display
from ipywidgets import interact, widgets

titanic = pd.read_csv('titanic.csv')
titanic.head()
data = titanic['Age']
mu = data.mean()
print('Mean',data.mean()) #Calculate mean
print('Mode',data.mode()) #Calculate mode
print('Median',data.median()) #Calculate Median
print('75th percentile',data.quantile(0.75)) #Calculate 75th percentile
sigma = np.std(data)
print('Sigma', sigma)

#histogram
data_list = list(data)
pp.hist(data_list, normed = 1, bins=50, facecolor = 'g',alpha = 0.75)
pp.xlabel('Age')
pp.ylabel('Probability')
pp.title('Histogram of Age')
pp.axis([0, 80, 0, 0.05])
pp.grid(True)
pp.show()

# Box plot
data.plot(kind = 'box')
pp.show()
