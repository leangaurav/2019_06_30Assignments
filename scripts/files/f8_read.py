with open('tables.txt', 'r') as f:
    print(f.tell())
    s = f.read() # not recommended
    print(f.tell())
    print(s)
    
    print("Read again:", f.read())