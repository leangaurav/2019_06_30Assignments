import sqlite3

conn = sqlite3.connect('temp.db')

def create_table():
    try:
        conn.execute('CREATE TABLE if not exists Contact(NAME TEXT NOT NULL PRIMARY KEY, PHONE TEXT NOT NULL, EMAIL TEXT)')
    except sqlite3.OperationalError:
        print('Table Exists')

create_table()


conn.close()

