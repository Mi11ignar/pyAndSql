import sqlite3

#Установка соединения с БД
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Выбор всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

#Вывод результатов
for user in users:
    print(user)

#Закрытие соединения
connection.close()