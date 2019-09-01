# names declared in a function are local to function
# i.e. they cannot be used outside the function.


def funct1():
    x = 1 # uses local x
    print(x)
    
def funct2():
    print(x) #uses global x

def funct3():
    global x # global keyword brings the global variable in current scope
    x = False
    print(x) #uses global x

x = True
funct1()
funct2()
print(x)
funct3()
print(x)