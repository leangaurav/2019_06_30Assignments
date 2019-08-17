f = open('normal.txt', 'r')
r = open('reverse.txt','w')
a = []
for line in f:
    for i in line:
        if i.isupper():
            a.append(i.lower())
		elif i.islower():
		    a.append(i.upper())
	line =(''.join(a))
    r.write(line)
f.close()
r.close()