import sqlite3

db = sqlite3.connect('sqlite_db.db')

# cursor object --> an object that is used to execute SQL statements

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE Employee(
        Employee int NOT NULL
        LastNa
    )
''')