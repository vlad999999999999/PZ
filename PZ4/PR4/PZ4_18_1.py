# PZ_2_18.py

#Кузнецов Влад

#Дано вещественное число X и целое число N>0. Найти значение
#выражения 1+X+X^2/2!+⋯+X^N/N!. Полученное число является приближенным
#значением функции exp(X).

x = float(input("Введите число X: "))
n = int(input("Введите число N (должно быть больше 0): "))

if n <= 0:  # Проверяем, что N больше 0
    print("Число N должно быть больше 0!")
    exit()

# Считаем сумму
result = 1  # Начальное значение суммы
for i in range(1, n + 1):
    faktorial = 1
    for j in range(1, i + 1):  # Считаем факториал вручную
        faktorial *= j
    result += (x ** i) / faktorial  # Добавляем к результату

# Вывод результата
print("Приближённое значение exp(X):", result)