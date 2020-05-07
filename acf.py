from pandas import read_csv
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('monthly-sunspots.txt').drop(['Month'],axis=1)#.head(100)
data_a = data.to_numpy().T[0]
data_a
plt.figure(figsize=(20,10))
plt.plot(data_a)

plt.rc("figure", figsize=(20,10))
plt.figure(figsize=(20,10))
plot_acf(data_a, lags=90)
plt.show()

data = pd.read_csv('AirPassengers.csv').drop(['Month'],axis=1)#.head(100)
data_a = data.to_numpy().T[0]
data_a
plt.figure(figsize=(20,10))
plt.plot(data_a)

plt.rc("figure", figsize=(20,10))
plt.figure(figsize=(20,10))
plot_acf(data_a, lags=50)
plt.show()
