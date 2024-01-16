import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Выбор первого пользователя
cursor.execute('SELECT * FROM Users')
first_user = cursor.fetchone()
print(first_user)

#Выбор первых 5ти пользователей
cursor.execute('SELECT * FROM Users')
first_five_users = cursor.fetchone()[5]
print(first_five_users)

#ВЫбор всех пользователей
cursor.execute('SELECT * FROM Users')
all_users = cursor.fetchall()
print(all_users)

connection.close()