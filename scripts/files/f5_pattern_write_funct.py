f = open('pattern1.txt', 'w')

for i in range(1,6):
    f.write('*'*i + '\n')
    
f.close()