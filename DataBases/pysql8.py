import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#выбор и сортировка поль-й по возрасту по убыванию
cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
results = cursor.fetchall()

for row in results:
    print(row)

connection.close()