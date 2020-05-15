import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('daily-total-female-births.csv',index_col=['Date'])
data['Births'][270] = 100
column = data['Births']
column.plot(figsize=(20,10))

data['Births'][270] = 100
column = data['Births']
column.plot(figsize=(20,10))

N = len(column)
time = np.arange(0,N)
(len(data),len(time))

#parameters
window_percentage = 20
k = int(len(column) * (window_percentage/100))
N = len(column)
(k,N)

column = column.to_numpy()

get_bands = lambda data : (np.mean(data) + 3*np.std(data),np.mean(data) - 3*np.std(data))
#get_bands = lambda data : (np.mean(data) + np.nanquantile(data,0.99),np.mean(data) - np.nanquantile(data,0.99))

bands = [get_bands(column[range(0 if i - k < 0 else i-k ,i + k if i + k < N else N)]) for i in range(0,N)]
upper, lower = zip(*bands)

# compute local outliers 
anomalies = (column > upper) | (column < lower)


# plotting...
plt.figure(figsize=(20,10))
plt.plot(time,column,'k',label='Data')
plt.plot(time,upper,'r-',label='Bands',alpha=0.3)
plt.plot(time,lower,'r-',alpha=0.3)

plt.plot(time[anomalies],column[anomalies],'ro',label='Anomalies')
plt.fill_between(time, upper, lower,facecolor='red',alpha=0.1)
plt.legend()

plt.show()
