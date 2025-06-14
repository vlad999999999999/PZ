# Практическое занятие №11 — Вариант 18
# Задание 2:
# 1. Вывести содержимое text18-18.txt
# 2. Посчитать знаки пунктуации в первых 4 строках
# 3. Создать новый файл, где строки идут в обратном порядке (как стих)

import string

try:
    dots = 0  # знаки пунктуации
    lines = []  # первые 4 строки

    f = open('text18-18.txt', encoding='utf-8')
    for i in range(4):
        line = f.readline()
        if not line:
            break
        lines.append(line)
        for ch in line:
            if ch in string.punctuation:
                dots += 1  # если символ знак

    rest = f.readlines()  # дочитываем всё остальное
    f.close()

    print(''.join(lines + rest))  # печатаем всё
    print('знаков пунктуации в первых 4 строках:', dots)

    all_lines = lines + rest
    rev = list(reversed(all_lines))  # реверс короч

    f2 = open('poem_out_18.txt', 'w', encoding='utf-8')  # пишем реверс
    f2.writelines(rev)
    f2.close()

except Exception as e:
    print('ошибка:', e) 
