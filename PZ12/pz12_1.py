# Практическое занятие №12 — Вариант 19
# Задание 1:
# В последовательности из n целых чисел найти среднее арифметическое первой трети

try:
    nums = [5, 12, -3, 8, 0, 7, 10, 6, 2]  # ну кароч список
    n = len(nums)
    one_third = nums[:n // 3]  # берём первую треть

    avg = sum(one_third) / len(one_third) if one_third else 0  # ср арифм, если есть что делить

    print('последовательность:', nums)
    print('первая треть:', one_third)
    print('среднее арифм первой трети:', avg)

except Exception as e:
    print('ошибка:', e)
