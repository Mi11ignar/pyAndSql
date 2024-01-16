import sqlite3

#Установка соединения с БД
connection = sqlite3.connection('my_database.db')
cursor = connection.cursor()

#Удаление пользователя
cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

#сохранение изменений и закрытие соединения
connection.commit()
connection.close()