import sqlite3

conn = sqlite3.connect('temp.db')

def create_table():
    try:
        conn.execute('CREATE TABLE if not exists Contact(NAME TEXT NOT NULL PRIMARY KEY, PHONE TEXT NOT NULL, EMAIL TEXT)')
    except sqlite3.OperationalError:
        print('Table Exists')

def get_data():
    curr = conn.execute('select * from Contact') # returns a cursor
    res = [data for data in curr]
    return res

def add_data(name,phone, email = ''):
    try:
        curr = conn.execute('INSERT into Contact VALUES (?,?,?)', (name, phone, email))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    return True
    

def cleanup(name):
    conn.execute('delete from Contact')
    return conn.rowcount == 1

def delete_data(name):
    res = conn.execute('delete from Contact where name like ?', (name,))
    conn.commit()
    return res.rowcount == 1

def update_name(old_name, new_name):
    try:
        res = conn.execute('update Contact set name = ? where name like ?', (new_name,old_name))
        conn.commit()
    except sqlite3.Error:
        return False
    return res.rowcount == 1
 
create_table()
print("\nData")
print(get_data())

res = add_data('abc','43243')
print("Add Data", res)

res = add_data('abcd','43243')
print("Add Data", res)

print("\n Update", update_name('abc','ABCDEF'))
print("\n Update", update_name('abc','ABCDEF'))

print("\n Deleting: ", delete_data('abcd'))
print("\n Deleting: ", delete_data('abcd'))

print("\nData")
print(get_data())


conn.close()

