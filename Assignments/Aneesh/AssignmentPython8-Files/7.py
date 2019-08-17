import sys
f = open(sys.argv[1], 'r')
d ={}
for line in f:
    print (line)
    for i in line:
	    d[i] = d.get(i, 0) + 1
print (d)