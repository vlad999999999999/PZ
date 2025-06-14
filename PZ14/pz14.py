# Практическое занятие №14 — Выборка файлов по расширению
# Задание:
# Из файла expansion.txt выбрать имена файлов, заканчивающиеся на:
# .xls, .xml, .html, .css, .py
# Посчитать их количество.

import re

try:
    # читаем файл
    with open('expansion.txt', encoding='utf-8') as f:
        text = f.read()

    # ищем файлы с нужным расширением
    pattern = r'\b[\w\-]+\.(xls|xml|html|css|py)\b'
    matches = re.findall(pattern, text, re.IGNORECASE)

    # теперь имена файлов с расширениями
    files = re.findall(r'\b[\w\-]+\.(?:xls|xml|html|css|py)\b', text, re.IGNORECASE)

    print('найденные файлы:')
    for name in files:
        print(name)

    print('всего файлов:', len(files))

except Exception as e:
    print('ошибка:', e)