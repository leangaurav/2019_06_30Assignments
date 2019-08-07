f = open('pattern.txt', 'w')

for i in range(1,6):
        print('*'*i, file = f)
    
f.close()