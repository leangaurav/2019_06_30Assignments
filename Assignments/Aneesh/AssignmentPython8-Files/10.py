import sys
f = open(sys.argv[1], 'r')
word = 0
for line in f:
    line = line.rstrip()
    a = line.split(' ')
    l = len(a)
    print (a)
    for i in range(0,l):
	    print (a[i])
	    print ( a[i][::-1])
	    if a[i] == a[i][::-1]:
	        word += 1
print ("Total number of palindromes in file is:",word)