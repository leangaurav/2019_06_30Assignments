f = open('file', 'w')
f.write('line with some characters')
f.close()

f = open('file', 'r')
print (f.tell())
print (f.read(4))
print (f.tell())
'''
0
line
4
'''