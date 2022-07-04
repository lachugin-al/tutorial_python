import sqlite3

con = sqlite3.connect('database.sqlite3')

# UPDATE DELETE DROP

with con:
#     con.execute("INSERT INTO notebook VALUES ('Maria', '8(911)111111', '30')")
    con.execute("INSERT INTO notebook VALUES ('Maria2', '8(911)111112', '32')")

# комитится каждый раз когда происходит execute в контекстном менеджере

    con.execute("UPDATE notebook SET phone = '+79111111111' WHERE name = 'Maria2'")
    con.execute("UPDATE notebook SET name = 'Irina', age = 20 WHERE name = 'Maria2'")

    # удаляем строку
    con.execute("DELETE FROM notebook WHERE name = 'Irina'")

    # удаляем таблицу
    # con.execute("DROP TABLE notebook")
con.close()