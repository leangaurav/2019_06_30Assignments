import sys
f = open(sys.argv[1], 'r')
count = 0
for line in f:
    print (line)
    for i in line:
	    if i ==' ':
		    count += 1
print ("Total spaces are:", count)
     
