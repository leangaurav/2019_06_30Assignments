import sys
f = open(sys.argv[1], 'r')
word = 0

for line in f:
    a = line.split(' ')
    print (a)
    word += len(a)
print ("Total number of words in file is:",word)
	    