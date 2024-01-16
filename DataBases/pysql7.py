import sqlite3

#создать соединение
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#получение среднеднего возраста поль-й ср-го возраста
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
results = cursor.fetchall()

for row in results:
    print(row)

#Фильтр группы по возрасту старше 30
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
filterd_results = cursor.fetchall()

for row in results:
    print(row)

connection.close()