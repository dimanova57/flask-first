import sqlite3

connection = sqlite3.connect('app.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE groceries 
               (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')
connection.commit()
connection.close()
