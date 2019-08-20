import math
import pandas as pd
import io
import numpy as np
import matplotlib
import matplotlib.pyplot as pp
import scipy.stats
import scipy.optimize
import scipy.spatial

bophieu = pd.read_csv('bophieu.csv')
bophieu.info()
bophieu.head()

data = bophieu.vote.value_counts(normalize = True)
green_vote = data[1]
def sample(green,n=1000):
    return pd.DataFrame({'vote':np.where(np.random.rand(n)>green,'Brown','Green')})
s = sample(green_vote,n =1000)
s.vote.value_counts(normalize =True)
dist = pd.DataFrame([sample(green_vote).vote.value_counts(normalize = True) for i in range(1000)])
dist.head()
dist.Green.hist(histtype = 'step',bins=20)
def samplingdist(green,n=1000):
    return pd.DataFrame([sample(green,n).vote.value_counts(normalize =True) for i in range(1000)])
def quantiles(green,n=1000):
    dist = samplingdist(green,n)
    return dist.Green.quantile(0.025), dist.Green.quantile(0.975)

print(quantiles(green_vote))
