# Практическое занятие №13 — Вариант 18
# Задание 1:
# В двумерном списке (матрице) увеличить в 3 раза те элементы, которые кратны 3

from random import randint

# генерим матрицу 4x4
m = [[randint(1, 20) for _ in range(4)] for _ in range(4)]

print('исходная матрица:')
for row in m:
    print(row)

# ну тут тупо каждый элемент чекаем и если %3 == 0 — х3
m_new = [[x * 3 if x % 3 == 0 else x for x in row] for row in m]

print('нью матрица:')
for row in m_new:
    print(row)
