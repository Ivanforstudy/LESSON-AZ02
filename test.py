

import pandas as pd

# Создаем DataFrame с данными
data = {
    'Имя': ['Аня', 'Борис', 'Вика', 'Дима', 'Елена', 'Женя', 'Игорь', 'Лена', 'Миша', 'Нина'],
    'Математика': [4, 5, 3, 4, 5, 2, 4, 3, 5, 4],
    'Русский язык': [3, 4, 4, 5, 3, 4, 3, 4, 5, 4],
    'История': [5, 5, 4, 3, 4, 5, 4, 3, 5, 4],
    'Физика': [4, 3, 5, 4, 3, 4, 5, 4, 2, 3],
    'Химия': [5, 4, 3, 4, 5, 3, 4, 5, 4, 3]
}

df = pd.DataFrame(data)

# Выводим первые несколько строк DataFrame
print("Первые строки DataFrame:")
print(df.head())

# Вычисляем среднюю оценку по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# Вычисляем медианную оценку по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"\nQ1 для математики: {Q1_math}")
print(f"Q3 для математики: {Q3_math}")

# Вычисляем IQR
IQR_math = Q3_math - Q1_math
print(f"IQR для математики: {IQR_math}")

# Вычисляем стандартное отклонение
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)
