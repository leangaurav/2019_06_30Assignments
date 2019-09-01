def creator(x):
    def funct():
        print(x)
        
    return funct
    
    
f1 = creator(10)
f1()
f1()

f2 = creator('ABCD')
f2()
f2()
f1()