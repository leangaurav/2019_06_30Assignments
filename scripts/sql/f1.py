import sqlite3

conn = sqlite3.connect('temp.db')

print(dir(conn))

conn.close()

