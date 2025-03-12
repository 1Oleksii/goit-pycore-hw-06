import pandas as pd

students_df = pd.DataFrame({
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
    'Вік': [21, 22, 20, 21, 23],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
}, index=['st1', 'st2', 'st3', 'st4', 'st5'])

# Вивести DataFrame
print(students_df)

# Описати статистику
print(students_df.describe())

value = students_df.loc['st2', 'Вік']
print(value) # 22

subset = students_df.loc['st2':'st4', 'Імена':'Вік']
print(subset) 

subset = students_df.loc[['st1', 'st3'], ['Імена', 'Спеціальність']]

    


print(value) # 22

subset = students_df.iloc[[0, 2], [0, 2]]
print(subset)

# Використання loc для вибору даних за мітками
bohdan_data = students_df.loc['st2', 'Спеціальність']
print(bohdan_data) # "Physics"

# Використання iloc для вибору даних за індексами
bohdan_data = students_df.iloc[1, 2]
print(bohdan_data) # "Physics"

import pandas as pd

students_df = pd.DataFrame({
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
    'Вік': [21, 22, 20, 21, 23],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
    }, index=['st1', 'st2', 'st3', 'st4', 'st5'])

value = students_df.loc['st2', 'Вік']
print(value) # 22

subset = students_df.loc['st2':'st4', 'Імена':'Вік']
print(subset) 

subset = students_df.loc[['st1', 'st3'], ['Імена', 'Спеціальність']]
print(subset)

value = students_df.iloc[1, 1]
print(value) # 22

subset = students_df.iloc[1:4, 0:2]
print(subset)

subset = students_df.iloc[[0, 2], [0, 2]]
print(subset)

# Використання loc для вибору даних за мітками
bohdan_data = students_df.loc['st2', 'Спеціальність']
print(bohdan_data) # "Physics"

# Використання iloc для вибору даних за індексами
bohdan_data = students_df.iloc[1, 2]
print(bohdan_data) # "Physics"

# Вибірка студентів, які вивчають фізику, за допомогою loc
physics_students = students_df.loc[students_df['Спеціальність'] == 'Physics']

# Вибірка студентів за конкретними індексами за допомогою iloc
specific_students = students_df.iloc[[1, 4]]

subset = students_df[1:3]
print(subset)

subset = students_df[3:]
print(subset)

subset = students_df[:2]
print(subset)

subset = students_df.loc[:, 'Імена':'Вік']
print(subset)

import pandas as pd

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
    'Вік': [21, 22, 20, 21, 23],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
}

students_df = pd.DataFrame(students_data)

grouped = students_df.groupby('Спеціальність')

mean_age = grouped['Вік'].mean()
print(mean_age)

mean_age = grouped['Вік'].mean()
print(mean_age)

min_max_age = grouped['Вік'].agg(['min', 'max'])
print(min_max_age)

summary = grouped.agg({
  'Вік': ['min', 'max', 'mean'],
  'Імена': 'count'
})
print(summary)

result = grouped['Вік'].agg(lambda x: x.max() - x.min())
print(result)

import pandas as pd

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
    'Вік': [21, 22, 20, 21, 23],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
}

students_df = pd.DataFrame(students_data)

total_age = students_df['Вік'].sum() # 107

average_age = students_df['Вік'].mean() # 21.4

std_age = students_df['Вік'].std() # 1.1401754250991378

import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

q1 = np.quantile(data, 0.25)  # 25% quantile
q2 = np.quantile(data, 0.50)  # 50% quantile (median)
q3 = np.quantile(data, 0.75)  # 75% quantile

print("Q1 (25% quantile):", q1)
print("Q2 (50% quantile - median):", q2)
print("Q3 (75% quantile):", q3)

import pandas as pd

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
    'Вік': [21, 22, 20, 21, 23],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
}

students_df = pd.DataFrame(students_data)

sorted_df = students_df.sort_values(by='Вік')
print(sorted_df)

sorted_df = students_df.sort_values(by='Спеціальність', ascending=False)
print(sorted_df)

sorted_df = students_df.sort_values(by=['Спеціальність', 'Вік'], ascending=[True, False])
print(sorted_df)

import pandas as pd

students_data = {
    'Імена': ['Anna', 'Bohdan', None],
    'Вік': [21, None, 20],
    'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

cleaned_df = students_df.dropna()
print(cleaned_df)

import numpy as np
import pandas as pd

data = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, np.nan, np.nan]])

data = data.fillna({0: data[0].mean(), 1: data[1].mean(), 2: data[2].mean()})

print(data)

import pandas as pd

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena'],
    'Вік': [21, 22, 20],
    'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

students_df.drop([1], inplace=True)
print(students_df)

import pandas as pd

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena'],
    'Вік': [21, 22, 20],
    'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

students_df = students_df.drop(['Вік'], axis=1)
print(students_df)

import pandas as pd

students_data = {
  'Імена': ['Anna', 'Bohdan', 'Olena'],
  'Вік': [21.0, 22.0, 20.0],# Вік як float
  'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

# Конвертація типу стовпця 'Вік' в int

students_df['Вік'] = students_df['Вік'].astype(int)
print(students_df.dtypes)

import pandas as pd

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena'],
    'Вік': [21, 22, 20],
    'Спеціальність': ['Math', 'PHYSICS', 'biology']
}

students_df = pd.DataFrame(students_data)

# Приведення спеціальностей до нижнього регістру
students_df['Спеціальність'] = students_df['Спеціальність'].str.lower()
print(students_df)

import pandas as pd

# Середні температури за дні місяця
temperature_data = {
    'День': list(range(1, 31)),
    'Температура': [15, 18, None, 20, 17, 18, 20, None, 14, 16, 18, 19, None, 15, 14, 17, 16, None, 17, 20, 15, 16, 15, 19, 20, None, 15, 18, 17, 16]
}

temperature_df = pd.DataFrame(temperature_data)

# Знаходження середньої температури за місяць, виключаючи відсутні значення
mean_temperature = temperature_df['Температура'].mean()

# Заміна відсутніх значень температури середньою температурою за місяць
temperature_df['Температура'].fillna(mean_temperature, inplace=True)
print(temperature_df)

import pandas as pd

data = {
    "name": ["Michael", "Steve", "Liza", "Jhon", "Liza", "Jhon"],
    "country": ["Canada", "USA", "Australia", "Denmark", "Australia", "Denmark"],
    "age": [25, 32, 19, 23, 19, 23]
}

employees = pd.DataFrame(data)

employees = employees.drop_duplicates()
print(employees)

import pandas as pd

data = {
    'Дата': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Температура': [25, 28, 24],
    'Вологість': ['висока', 'низька', 'висока']
}

weather_df = pd.DataFrame(data)


weather_df['Вологість'].replace({'висока': 80, 'низька': 30}, inplace=True)

import pandas as pd

date = pd.Timestamp("2021-09-10")

print(date)# 2021-09-10 00:00:00

import pandas as pd

date = pd.date_range(start='2021-09-01', freq='D', periods=8)

temperature = pd.Series([23, 17, 17, 16, 15, 14, 17, 20], index=date)

print(temperature)

data = {
    'Місто': ['Київ', 'Львів', 'Одеса', 'Харків', None, 'Львів'],
    'Температура': [25, 32, None, 24, 23, 32],
    'Вологість': ['60%', '70%', '65%', '55%', None, '70%'],
    'Дата': ['2021-08-01', '2021-08-01', '2021-08-02', '2021-08-02', '2021-08-03', '2021-08-01']
}
df = pd.DataFrame(data)
print(df)

df.drop_duplicates(subset=['Місто', 'Дата'], inplace=True)

df.dropna(subset=['Місто'], inplace=True)
df['Температура'].fillna(df['Температура'].mean(), inplace=True)

df['Вологість'] = df['Вологість'].str.rstrip('%').astype('float') / 100
df['Дата'] = pd.to_datetime(df['Дата'])

import pandas as pd  

# Початкові дані  
data = {
    'Місто': ['Київ', 'Львів', 'Одеса', 'Харків', None, 'Львів'],
    'Температура': [25, 32, None, 24, 23, 32],
    'Вологість': ['60%', '70%', '65%', '55%', None, '70%'],
    'Дата': ['2021-08-01', '2021-08-01', '2021-08-02', '2021-08-02', '2021-08-03', '2021-08-01']
}

df = pd.DataFrame(data)

# Видаляємо дублікати
df.drop_duplicates(subset=['Місто', 'Дата'], inplace=True)

# Видаляємо рядки з пустими містами
df.dropna(subset=['Місто'], inplace=True)

# Заповнюємо відсутні значення температури середнім значенням
df['Температура'].fillna(df['Температура'].mean(), inplace=True)

# Конвертуємо "Вологість" у число
df['Вологість'] = df['Вологість'].astype(str).str.rstrip('%').replace('None', None).astype(float) / 100

# Конвертуємо "Дата" у формат datetime
df['Дата'] = pd.to_datetime(df['Дата'], errors='coerce')

# Вивід очищеного DataFrame
print(df)

import pandas as pd

data1 = {
    "name": {"1": "Michael", "2": "John"},
    "country": {"1": "Canada", "2": "USA"},
    "age": {"1": 25, "2": 32}
}

employees1 = pd.DataFrame(data1)

data2 = {
    "name": {"3": "Liza", "4": "Jhon"},
    "country": {"3": "Australia", "4": "Denmark"},
    "age": {"3": 19, "4": 23}
}

employees2 = pd.DataFrame(data2)

employees = pd.concat([employees1, employees2])

print(employees)

import pandas as pd

data1 = {
    "name": ["Michael", "John"],
    "country": ["Canada", "USA"],
}

data2 = {
    "name": ["Michael", "Liza"],
    "age": [25, 19]
}

employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)

merged = pd.merge(employees1, employees2, on='name', how='outer')
print(merged)

merged = pd.merge(employees1, employees2, on='name', how='inner')
print(merged)

import pandas as pd

data1 = {
    "name": {"1": "Michael", "2": "John", "3": "Liza", "4": "Jhon"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia", "4": "Denmark"}
}

data2 = {
    "age": {"1": 25, "2": 32, "3": 19, "4": 23}
}

employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)

joined = employees1.join(employees2)
print(joined)

import pandas as pd

data1 = {
    "name": ["Michael", "John"],
    "country": ["Canada", "USA"],
}

data2 = {
    "name": ["Michael", "Liza"],
    "age": [25, 19]
}

employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)

employees2 = employees2.set_index("name")

joined = employees1.join(employees2, on="name", how="outer")
print(joined)

employees1 = pd.DataFrame(data1).set_index("name")
employees2 = pd.DataFrame(data2).set_index("name")

joined = employees1.join(employees2, how="outer")
print(joined)

import pandas as pd

data = {
    'Дата': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Температура C': [25, 28, 24]
}

weather_df = pd.DataFrame(data)

weather_df['Температура F'] = weather_df['Температура C'].apply(lambda temp: (temp * 9/5) + 32)

weather_df['Температура F'] = weather_df['Температура C'].apply(lambda temp: (temp * 9/5) + 32)

print(df)

import pandas as pd

# Дані про продукти та їх ціни та знижки
data = {
    'Product': ['iPhone 13', 'MacBook Pro', 'Apple Watch'],
    'Price': [699, 1299, 399],
    'Discount': [0.1, 0.05, 0.15]
}

# Створення DataFrame з цими даними
df = pd.DataFrame(data)

# Застосування lanbda-функції до кожного рядка за допомогою apply з axis=1
df['Final Price'] = df.apply(lambda row: row['Price'] * (1 - row['Discount']), axis=1)

print(df)

import pandas as pd

# Дані про товари та їх ціни
data = {
    'iPhone 13 (64GB)': [699, 799],
    'MacBook Pro (13-inch)': [1299, 1499]
}

# Створення DataFrame з цінами
df = pd.DataFrame(data)

# Застосування 10% знижки до всіх цін за допомогою applymap і лямбда-функції
df_discounted = df.applymap(lambda price: price * 0.9)

print(df_discounted)

import pandas as pd
df = pd.DataFrame({
  "Фрукт": ["Яблуко", "Яблуко", "Груша", "Груша", "Банан", "Банан"],
  "Колір": ["Червоний", "Зелений", "Жовтий", "Зелений", "Жовтий", "Зелений"],
  "Кількість": [10, 12, 15, 9, 20, 18],
  "Ціна": [5, 4, 6, 7, 3, 2]
})
print(df)




