#Kütüphaneler
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype

#Veri Setini Yükle
df_newyork = pd.read_csv("AB_NYC_2019.csv")

#Veri seti hakkında bilgiler
headd = df_newyork.head()
inf = df_newyork.info()
colmns = df_newyork.columns
shpe = df_newyork.shape

print(headd)
print(inf)
print(colmns)
print(shpe)

#name kolonu value counts
value_count = df_newyork['name'].value_counts()
print(value_count)


#isnull değerler var mı
snll = df_newyork.isnull().sum()
print(snll)


#dtype object olmayanların listesi
numeric_colmn = df_newyork.select_dtypes(exclude=['object']).columns.tolist()
# print(df_newyork[numeric_colmn])

#sayısal veriler hakkında bilgi
descri = df_newyork[numeric_colmn].describe()

#numeric colunlar price göre scatterplot
cols = numeric_colmn

for col in cols:
  plt.figure(figsize=(5,5))
  sns.scatterplot(x=col, y="price", data=df_newyork)
  plt.show()
  
#price ayrık değerler
df_newyork['price'].plot(kind='box', vert=False, figsize=(15,3))
plt.show()

# Price histplot
sns.histplot(df_newyork["price"], kde=True)
plt.show()

#histogram
his = df_newyork[numeric_colmn].hist(figsize=(15,10))
plt.show()

#corr
sns.heatmap(df_newyork.corr(), annot=True);
plt.show()

#hangi oda türünden kaç adet var
room_count = df_newyork['room_type'].value_counts().sort_values(ascending=False)
print(room_count)

room_count.plot.bar().set_title("Room type Variable Numbers")
plt.show()
















