import sqlite3

#Установка соединения с БД
connection =sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Обновление возраста пользователя 'newuser'
cursor.execute('UPDATE Users SET age = ? WHERE username', (29, 'newuser'))

#Сохранения изменений и закрытие соединения
connection.commit()
connection.close()