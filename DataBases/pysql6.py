import sqlite3

#Создание соединения
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Выбор имени и возраста поль-й старше 25
cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
results = cursor.fetchall()

for row in results:
    print(row)

#Закрыть соединение
connection.close()