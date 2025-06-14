#Кузнецов Влад

N = int(input("Введите размер списка: "))

R = int(input("Введите число R: "))

A = []

# Вводим элементы списка
for i in range(N):
    num = int(input(f"Введите элемент {i + 1}: "))
    A.append(num)  # Добавляем число в список

print("Ваш список:", A)

min_diff = 999999999

best_num1 = None
best_num2 = None

for i in range(N):  # Перебираем первый элемент пары
    for j in range(i + 1, N):  # Перебираем второй элемент
        diff = abs(A[i] + A[j] - R)  # Считаем разницу между суммой пары чисел и числом R
        if diff < min_diff:
            min_diff = diff  # Новая минимальная разница
            best_num1 = A[i]  # Первое число
            best_num2 = A[j]  # Второе число

print(f"Элементы списка, чья сумма наиболее близка к числу {R}: {best_num1} и {best_num2}")
