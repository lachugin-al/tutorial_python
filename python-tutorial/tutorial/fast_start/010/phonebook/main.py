import sqlite3


# создаем подключение и возвращаем его
def get_connection():
    con = sqlite3.connect('phonebook.sqlite3')
    con.execute("CREATE TABLE IF NOT EXISTS data (name TEXT, surname TEXT, phone INTEGER)")
    return con


def get_cursor(con):
    curson = con.cursor()
    return curson


# вставляем данные через кортеж
# через формат строки вставлять данные небезопасно
def insert_data(cursor, name, surname, phone):
    cursor.execute("INSERT INTO data VALUES (?, ?, ?)", (name, surname, phone,))
    con.commit()
    print('Данные успешно добавлены в записную книжку')


# получаем курсор и выводим данные построчно
def show_data(cursor):
    cursor.execute("SELECT * FROM data")
    for element in cursor.fetchall():
        print(element)  # в виде кортеж
        print(*element)  # в виде распакованного кортеж


def delete_by_name(cursor, name):
    cursor.execute("DELETE FROM data WHERE name = ?", (name,))
    con.commit()
    print('Данные успешно удалены из записной книжки')


if __name__ == '__main__':
    print('Добро пожаловать в записную книжку')

    action = None
    while action != 'exit':
        con = get_connection()  # получаем подключение
        cursor = get_cursor(con)  # получаем курсор
        action = input('Выберите действие [add, read, delete]\n').strip()
        if action == 'add':
            try:
                name, surname, phone = input('Введите данные (name, surname, phone): ').split(' ')
            except ValueError:
                print('Неверно введенные данные')
            else:
                insert_data(cursor, name, surname, phone)
        elif action == 'read':
            show_data(cursor)
        elif action == 'delete':
            name_to_delete = input('Введите имя контакта для удаления: ')
            delete_by_name(cursor, name_to_delete)
        else:
            con.close()  # закрываем коннекшен
            print('Удачного дня')
            exit(0)
