f = open('alphabet.txt', 'w')
for i in range(65,91):
        print(chr(i), file = f)
    
f.close()