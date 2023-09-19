import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('arquivo.csv')
df = df.drop(df.columns[0], axis=1)
eixo_x= df['MAIN_GENRE'].value_counts().keys()
eixo_y=df['MAIN_GENRE'].value_counts().values
plt.barh(eixo_x, eixo_y)
plt.show()