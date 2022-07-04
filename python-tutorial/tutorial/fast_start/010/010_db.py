import sqlite3

# создает коннекшен и через него создаем файл базы данных
connection = sqlite3.connect('database.sqlite3')

# CRUD
# необходимо получить курсор для работы с базой
cursor = connection.cursor()

# создание таблицы
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notebook (
    name TEXT,
    phone TEXT,
    age INTEGER)
""")

# добавление данный в таблицу
cursor.execute("INSERT INTO notebook VALUES ('Anton', '+79111111111', 42)")

# комитим внесенные добавления в базу
connection.commit()

cursor.execute("SELECT * FROM notebook")

# получить даныне и вывести построчно
for el in cursor.fetchall():
    print(el)

# закрываем соединение после завершени работы с базой
connection.close()

