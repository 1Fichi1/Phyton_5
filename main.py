import pandas as pd
import numpy as np

# Загрузка датасета
Mall_Customers = pd.read_csv('Mall_Customers.csv')
Mall_Customers

# вывод
Mall_Customers.head()

# размерность массива
Mall_Customers.shape

# вывод намименований всех колонок
Mall_Customers.columns

# Вывод всех уникальных значений
Mall_Customers['Spending Score (1-100)'].unique()

# Отсортировка по определенным параметрам
Mall_Customers.sort_values(by='CustomerID')

# Удаление ненужных столбцов или строк
Mall_Customers.drop(columns = ["Genre"], inplace=True)

# Заменение определенных значений в датасете (например, пустые)
Mall_Customers["Age"] = Mall_Customers["Age"].replace(Mall_Customers["Age"].unique(), "immortal")
Mall_Customers

# Удаление дубликатов
Mall_Customersa = Mall_Customers.drop_duplicates()
Mall_Customers

# Проведение анализов с помощью функций info
Mall_Customers.info()

# Проведение анализа с помощью функций describe
Mall_Customers.describe()

# Проведение выборки данных по строкам и столбцам с помощью loc
subset = Mall_Customers.loc[[0, 1, 2], ['Annual Income (k$)', 'Spending Score (1-100)']]
subset

# Сохранение нового датасетаa
Mall_Customers.to_csv("Mall_Customers_NEW.csv", index=True)
Mall_Customers


