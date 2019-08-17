import sys
f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'r')
same = True
f =list(f)
print (f)
g = list(g)
print (g)

for i in range(0, len(f)):
        if f[i] == g[i]:
            print ("Line",i,"is same")   
        else:
            same = False
if same == True:
    print ("Files are same")
else:
    print ("Files are different")