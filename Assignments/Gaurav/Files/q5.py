with open('textfile1.txt', 'r') as f1:
    with open('textfile1copy.txt', 'w') as f2:
        for line in f1:
            f2.write(line.swapcase())
            
            
with open('textfile1.txt', 'r') as f1:
    with open('textfile1copy.txt', 'w') as f2:
        for line in f1:
            for c in line:
                if c.islower():
                    c = c.upper()
                else:
                    c = c.lower()
                f2.write(c)