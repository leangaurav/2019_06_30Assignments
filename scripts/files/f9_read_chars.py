with open('tables.txt', 'r') as f:

    
    print(f.tell())
    s = f.read(5)
    while s:
        print(s, f.tell(),end = '')
        s = f.read(5)
        
    print("\n\nReReading \n")
    f.seek(0) # 0 pos from beginning
    s = f.read(20)
    while s:
        print(s, f.tell(),end = '')
        s = f.read(20)