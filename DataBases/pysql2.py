import sqlite3

#Установка соединения с БД
connection =sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Создание индекса для столбца "email"
cursor.execute('CREATE INDEX idx_email ON Users (email)')

#Сохранения изменений и закрытие соединения
connection.commit()
connection.close()