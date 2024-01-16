import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Выбор ползователей с неизвестным возрастом
cursor.execute('SELECT * FROM Users WHERE age IS NULL')
unkown_age_users = cursor.fetchall()

#Вывод результатов
for user in unkown_age_users:
    print(user)

connection.close()