import pandas as pd

taxis = pd.read_csv('taxis.csv')
taxis.head()
taxis['dropoff_borough'].value_counts()
