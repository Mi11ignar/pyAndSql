#Импорт БД
import sqlite3

#Установка соединения с БД(файл 'my_database.db') будет создан
connection =sqlite3.connect('my_database.db')

#Закрытие соединения
connection.close()