# Практическое занятие №12 — Вариант 19
# Задание 2:
# Сделать генератор, который переводит все буквы в строке в заглавные (через yield)

def upcase_gen(text):
    for ch in text:
        if ch.isalpha():  # если буква
            yield ch.upper()  # кароч возвращаем заглавную
        else:
            yield ch  # остальное как было

try:
    s = 'привет, как дела? 123abc!'  # ну типо строка
    result = ''.join(upcase_gen(s))  # склеиваем результат генератора

    print('оригинал:', s)
    print('результат:', result)

except Exception as e:
    print('ошибка:', e)
