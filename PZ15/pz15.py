# практическое занятие №15 — вариант 18
# тема: страховая компания, таблица договор
# записываем 10 штук, ищем, удаляем, редачим
# таблица: дата, сумма, тип, ставка, филиал

import sqlite3

# подключение к бд
con = sqlite3.connect("strah.db")
cur = con.cursor()

# создаём таблицу если нет
cur.execute("""CREATE TABLE IF NOT EXISTS dogovor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    amount REAL,
    type TEXT,
    rate REAL,
    branch TEXT
)""")
con.commit()

# добавление
cur.execute("INSERT INTO dogovor (date, amount, type, rate, branch) VALUES ('2024-01-01', 100000, 'Жизнь', 0.05, 'Ростов')")
cur.execute("INSERT INTO dogovor (date, amount, type, rate, branch) VALUES ('2024-01-05', 80000, 'Авто', 0.04, 'Москва')")
cur.execute("INSERT INTO dogovor (date, amount, type, rate, branch) VALUES ('2024-01-10', 50000, 'Имущество', 0.03, 'Питер')")
cur.execute("INSERT INTO dogovor (date, amount, type, rate, branch) VALUES ('2024-02-01', 120000, 'Жизнь', 0.05, 'Казань')")
cur.execute("INSERT INTO dogovor (date, amount, type, rate, branch) VALUES ('2024-02-10', 60000, 'Авто', 0.04, 'Москва')")
cur.execute("INSERT INTO dogovor (date, amount, type, rate, branch) VALUES ('2024-02-15', 45000, 'Имущество', 0.03, 'Ростов')")
cur.execute("INSERT INTO dogovor (date, amount, type, rate, branch) VALUES ('2024-03-01', 90000, 'Жизнь', 0.05, 'Питер')")
cur.execute("INSERT INTO dogovor (date, amount, type, rate, branch) VALUES ('2024-03-10', 70000, 'Авто', 0.04, 'Казань')")
cur.execute("INSERT INTO dogovor (date, amount, type, rate, branch) VALUES ('2024-04-01', 110000, 'Жизнь', 0.05, 'Ростов')")
cur.execute("INSERT INTO dogovor (date, amount, type, rate, branch) VALUES ('2024-04-15', 75000, 'Имущество', 0.03, 'Москва')")
con.commit()

# поиск 1: по типу
print("фильтр: тип = Жизнь")
cur.execute("SELECT * FROM dogovor WHERE type = 'Жизнь'")
for x in cur.fetchall():
    print(x)

# поиск 2: сумма больше 100к
print("фильтр: сумма > 100000")
cur.execute("SELECT * FROM dogovor WHERE amount > 100000")
for x in cur.fetchall():
    print(x)

# поиск 3: филиал = Ростов
print("фильтр: филиал = Ростов")
cur.execute("SELECT * FROM dogovor WHERE branch = 'Ростов'")
for x in cur.fetchall():
    print(x)

# удаление 1: тип авто
cur.execute("DELETE FROM dogovor WHERE type = 'Авто'")
print("удалено: тип авто")

# удаление 2: ставка < 0.04
cur.execute("DELETE FROM dogovor WHERE rate < 0.04")
print("удалено: ставка < 0.04")

# удаление 3: филиал Питер
cur.execute("DELETE FROM dogovor WHERE branch = 'Питер'")
print("удалено: филиал питер")

# редакт 1: ставка = 0.07 где сумма > 100000
cur.execute("UPDATE dogovor SET rate = 0.07 WHERE amount > 100000")
print("обновлено: ставка 0.07 где сумма > 100к")

# редакт 2: филиал = Тула где тип = Жизнь
cur.execute("UPDATE dogovor SET branch = 'Тула' WHERE type = 'Жизнь'")
print("обновлено: филиал = тула где жизнь")

# редакт 3: сумма = 99999 где id = 1
cur.execute("UPDATE dogovor SET amount = 99999 WHERE id = 1")
print("обновлено: сумма = 99999 где id 1")

con.commit()

# вывод всего
print("текущие записи:")
cur.execute("SELECT * FROM dogovor")
for x in cur.fetchall():
    print(x)

con.close()
