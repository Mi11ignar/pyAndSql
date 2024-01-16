import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#нахождение поль-й с наибольшим возрастом
cursor.execute('''
               SELECT username, age
               FROM Users
               WHERE age = (SELECT Max(age) FROM Users)
               ''')
oldest_users = cursor.fetchall()

#Вывод результатов
for user in oldest_users:
    print(user)

#Закрыть соединение
connection.close()