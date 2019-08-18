f = open('normal.txt', 'r')
r = open('reverse.txt','w')
a = []
for line in f:
<<<<<<< HEAD
	for i in line:
		if i.isupper():
			a.append(i.lower())
		else :
			a.append(i.upper())

	line =(''.join(a))
	r.write(line)
=======
    for i in line:
        if i.isupper():
            a.append(i.lower())
        elif i.islower():
            a.append(i.upper())
    line =(''.join(a))
    r.write(line)
>>>>>>> eb4b827eebabdf15b0947bfaa8fa48b6770e2bbc
f.close()
r.close()

	


