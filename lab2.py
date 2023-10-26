
#%%
import psycopg2

import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
# %matplotlib inline     
sns.set(color_codes=True)

# Define connection parameters
conn = psycopg2.connect(
   host = "localhost",
database = "mtcars",
user = "postgres",
password = "0000" 
)



query = "SELECT * FROM mtcars;"
df = pd.read_sql_query(query, conn)

print(df)
#%%

print(df.head())

# Анализ количества и качества данных
print("Информация о данных:")
print(df.info())

# Статистический анализ числовых данных
print("Основные статистические показатели:")
print(df.describe())


df.hist()
plt.show()


#%%
# Найдите самую дорогую машину (максимальный вес)
max_wt_car = df[df['wt'] == df['wt'].max()]

print("Самая дорогая машина:")
print(max_wt_car)
#%%

df.tail(5)

# %%
df.tail(5)
# %%

df.dtypes
# %%

df = df.drop(['hp', 'drat'], axis=1) # удалил столбец hp,drat
df.head(5)
# %%

df.shape
# %%

duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)
# %%

df.count()
# %%
df = df.drop_duplicates()
df.head(5)
# %%

print(df.isnull().sum())
# %%

df = df.dropna()    # Dropping the missing values.
df.count()
# %%

sns.boxplot(x=df['mpg'])
# %%

