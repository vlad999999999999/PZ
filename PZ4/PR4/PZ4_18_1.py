# PZ_2_18.py

#Кузнецов Влад

#Дано вещественное число X и целое число N>0. Найти значение
#выражения 1+X+X^2/2!+⋯+X^N/N!. Полученное число является приближенным
#значением функции exp(X).

import math

try:
    x = float(input("Введите вещественное число X: "))
    n = int(input("Введите целое число N (> 0): "))
    if n <= 0:
        raise ValueError
except ValueError:
    print("Неправильный ввод!")
    exit(1)

result = 1
for i in range(1, n + 1):
    result += x**i / math.factorial(i)
print(f"Приближенное значение функции exp в точке X: {result}")
