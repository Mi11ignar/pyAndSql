#Импорт БД
import sqlite3

#Установка соединения с БД
connection =sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Создание таблицы
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Users (
               id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               email TEXT NOT NULL,
               age INTEGER
               )
               ''')

#Сохранение изменения
connection.commit()
#Закрыть соединение
connection.close()