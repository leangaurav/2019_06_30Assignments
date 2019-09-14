from contact import Contact
from contact_manager import ContactManager

mgr = ContactManager()

main_menu = """ MAIN MENU
1. View
2. Add
3. Delete 
4. Update
5. Exit
"""

view_menu = """View
1. By Name
2. Pattern
3. View All
"""

def view():
    print(view_menu)
    ch = input_option(1,3)
    
    if ch == 1:
        pass
    elif ch == 2:
        pass
    else:
        pass

def add():
    name = input('Enter name :')
    phone = input('Enter phone :')
    email = input('Enter email :')

    c = Contact(name, phone, email)
    res = mgr.add_contact(c)
    if res:
        print('Added Successfully !!')
    else:
        print('Addition Failed !!')
    
def delete():
    name = input('Enter Name to Delete : ')
    res = mgr.delete_contact(name)
    if res:
        print('Deleted SUccessfully !!')
    else: 
        print('Unable to delete !!')

def update():
    pass

def input_option(start, end):
    while True:
        ch = input('Enter Choice({} - {}):'.\
                format(start, end))
        if ch.isdigit():
            ch = int(ch)
            if start <= ch <= end:
                return ch
        print('Invalid Input !!')

def main():
    while True:
        print(main_menu)
        ch = input_option(1,5)
        a = [view, add, delete, update, exit]
        a[ch - 1]()


if __name__ == '__main__':
    main()