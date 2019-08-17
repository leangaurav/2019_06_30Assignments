import sys
f = open(sys.argv[1], 'r')
word = 0
print (f)
for line in f:
    print (line)
    a = line.split(' ')
	#print(a)
	for i in a:
	    x = i.split('')
		word += len(x)
print ("Total words in file is:", word)