# Практическое занятие №13 — Вариант 18
# Задание 2:
# Найти среднее арифметическое элементов последних двух столбцов матрицы

from random import randint

# делаем матрицу 4x5
m = [[randint(1, 10) for _ in range(5)] for _ in range(4)]

print('матрица:')
for row in m:
    print(row)

# собираем все значения из последних двух столбцов
last_cols = [row[-2:] for row in m]  # берём последние 2 столбца у каждой строки
flat = [num for pair in last_cols for num in pair]  # разворачиваем в 1 список

avg = sum(flat) / len(flat) if flat else 0  # считаем ср арифм

print('элементы последних двух столбцов:', flat)
print('среднее арифметическое:', avg)
