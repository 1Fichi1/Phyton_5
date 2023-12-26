# Импорт библиотек Pandas и NumPy
import pandas as pd
import numpy as np

# Загрузка данных из файла 'Mall_Customers.csv' в DataFrame
Mall_Customers = pd.read_csv('Mall_Customers.csv')
Mall_Customers

# Вывод первых нескольких строк (5) из DataFrame
Mall_Customers.head()

# Вывод размерности (количество строк и столбцов) DataFrame
Mall_Customers.shape

# Вывод списка названий всех столбцов DataFrame
Mall_Customers.columns

# Вывод уникальных значений из столбца 'Spending Score (1-100)'
Mall_Customers['Spending Score (1-100)'].unique()

# Сортировка данных по столбцу 'CustomerID'
Mall_Customers.sort_values(by='CustomerID')

# Удаление столбца 'Genre' из DataFrame
Mall_Customers.drop(columns = ["Genre"], inplace=True)

# Замена всех уникальных значений в столбце 'Age' на "immortal"
Mall_Customers["Age"] = Mall_Customers["Age"].replace(Mall_Customers["Age"].unique(), "immortal")
Mall_Customers

# Создание нового DataFrame Mall_Customersa, в котором удалены дубликаты
Mall_Customersa = Mall_Customers.drop_duplicates()
Mall_Customers

# Вывод общей информации о DataFrame
Mall_Customers.info()

# Вывод основных характеристик данных в DataFrame
Mall_Customers.describe()

# Создание подмножества данных, выбирая строки 0, 1, 2 и столбцы 'Annual Income (k$)' и 'Spending Score (1-100)'
subset = Mall_Customers.loc[[0, 1, 2], ['Annual Income (k$)', 'Spending Score (1-100)']]
subset

# Сохранение нового датасетаa
Mall_Customers.to_csv("Mall_Customers_NEW.csv", index=True)
# Вывод исходного DataFrame.
Mall_Customers


