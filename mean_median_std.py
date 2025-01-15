import pandas as pd


#data = {
#    'Набор А': [85, 90, 95, 100, 105],
#    'Набор Б': [70, 80, 95, 110, 120],
#}

#Создаём датафрейм:

#df = pd.DataFrame(data)

#Вычислим стандартное отклонение в данных наборах, чтобы увидеть,
# насколько сильно значения в наборе данных отличаются от среднего значения.
# Для этого используем функцию std. Для начала создадим переменные для наборов данных:

#stdA = df['Набор А'].std()
#stdB = df['Набор Б'].std()
#print(f"Стандартное отклонение 1 набор - {stdA}")
#print(f"Стандартное отклонение 2 набор - {stdB}")

#Поработаем одновременно с несколькими мерами, о которых мы говорили в теоретической части.

#1. Создадим тематический набор информации:

data = {
    'Возраст': [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
    'Зарплата': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000],
}
df = pd.DataFrame(data)
#print(df.describe())

#В окне вывода мы видим количество возрастов, количество зарплат, средний возраст,
# среднюю зарплату, стандартное отклонение, минимальное, медианное и максимальное значение
# — всё в одном массиве текста. Выведем эти значения по отдельности

print(f"Средний возраст - {df['Возраст'].mean()}")
print(f"Медианный возраст - {df['Возраст'].median()}")
print(f"Стандартное отклонение возраста - {df['Возраст'].std()}")

print(f"Средняя зарплата - {df['Зарплата'].mean()}")
print(f"Медианная зп - {df['Зарплата'].median()}")
print(f"Стандартное отклонение зп - {df['Зарплата'].std()}")