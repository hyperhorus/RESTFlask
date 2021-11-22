import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)


connection.commit()

query = "SELECT * FROM sqlite_master WHERE type='table'"
for row in cursor.execute(query):
    print((row))
connection.close()