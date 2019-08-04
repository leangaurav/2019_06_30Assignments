

with open('tables.txt', 'w') as f:
    for i in range(1,11):
        #print(i, 'x', 3, '=', i*3, sep = '', file = f)
        f.write( '%iX3=%i\n' %(i,i*3))
