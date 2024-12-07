# Кузнецов Влад

import random

# Функция для генерации числа и проверки на одинаковые цифры
def check_same_digits():
    # Генерируем случайное четырехзначное число
    number = random.randint(1000, 9999)
    print(f"Сгенерированное число: {number}")

    # Преобразуем число в строку для работы с его цифрами
    num_str = str(number)

    # Проходимся по всем числам числа
    for i in range(len(num_str)):
        # Проходимся ещё раз но используем + 1 что бы не проверяь одинаковые цифры в одном и том же месте
        for j in range(i + 1, len(num_str)):
            if num_str[i] == num_str[j]:
                print(f"Число {number} содержит одинаковые цифры!")
                return
    print(f"Число {number} не содержит одинаковых цифр.")

# Вызов функции
check_same_digits()
