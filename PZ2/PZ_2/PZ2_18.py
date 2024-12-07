# PZ_2_18.py

# Вариант 18. Дано трехзначное число. В нем зачеркнули первую слева цифру и
# приписали ее справа. Вывести 

#Кузнецов Влад

try:
    # Вводим трехзначное число
    number = int(input("Введите трехзначное число: "))

    # Проверяем, что число трехзначное
    if 100 <= number <= 999:
        # Переставляем цифры: переносим первую цифру в конец
        new_number = (number % 100) * 10 + number // 100
        
        # Вывод результата
        print("Результат:", new_number)
    else:
        print("Ошибка: введено не трехзначное число.")
except ValueError:
    print("Ошибка: введите корректное целое число.")

