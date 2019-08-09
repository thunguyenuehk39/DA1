import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#a
plt.plot(['2015','2016','2017','2018'],[3,4,5,6])
plt.ylabel('increase')
plt.xlabel('year')
plt.show()

#b
with open("data_file.txt") as f:
	mylist = f.readlines()

x= [line.split()[0] for line in mylist]
y= [line.split()[1] for line in mylist]

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Plot title")
ax1.set_xlabel('x label')
ax1.set_ylabel('y label')

ax1.plot(x,y, 'ro', label = 'the data')

leg = ax1.legend()

plt.show()

#c

df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11)})

plt.plot( 'x', 'y1', data=df, marker='', color='olive', linewidth=2)
plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
plt.show()

#d
N = 500
x = np.random.rand(N)
y = np.random.rand(N)
colors = (0,0,0)
area = np.pi*3

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
