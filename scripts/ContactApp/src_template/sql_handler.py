from functools import wraps
import sqlite3
from contact import Contact

class SQLHandler:
    # TODO: add class attributes here

    def __init__(self, db_name):
        self.__conn = sqlite3.connect(db_name)
        self.__create_db()

    def __del__(self):
        self.__conn.close()
        self.__conn = None
    
    def cleanup_db(self):            
        self.__conn.execute('delete from Contact')
        
    def __create_db(self):
        try:
            self.__conn.execute('CREATE TABLE if not exists Contact(NAME TEXT NOT NULL PRIMARY KEY, PHONE TEXT NOT NULL, EMAIL TEXT)')
        except sqlite3.OperationalError:
            print('Table Exists')

    def get_contacts(self):
        curr = self.__conn.execute('select * from Contact') # returns a cursor
        res = [Contact(data[0], data[1], data[2]) for data in curr]
        return res

    
    def add_contact(self, contact_data):
        try:
            curr = self.__conn.execute('INSERT into Contact VALUES (?,?,?)', (contact_data.name, contact_data.phone, contact_data.email))
            self.__conn.commit()
        except sqlite3.IntegrityError:
            return False
        return True

    def delete_contact(self, contact_name):
        res = self.__conn.execute('delete from Contact where name like ?', (contact_name,))
        self.__conn.commit()
        return res.rowcount == 1

    def update_contact(self, old_data, new_data):
        # TODO: Execute Update Query to udpate data. 
        pass
    
if __name__ == "__main__":
    mgr = SQLHandler('dummy.db')
    mgr.cleanup_db()
    print(mgr)
    print(mgr.get_contacts())
    
    c1 = Contact("Gaurav","9999999999","tuteur.py@gmail.com")
    c2 = Contact("Krishna","8888888888","krishna.cpp@gmail.com")
    print(mgr.add_contact(c1))
    print(mgr.add_contact(c2))
    
    for contact in mgr.get_contacts():
       print(contact)
    
    print()
    print("Delete Krishna: ", mgr.delete_contact("Krishna"))
    print("Delete Krishna Again: ", mgr.delete_contact("Krishna"))
    for contact in mgr.get_contacts():
       print(contact)