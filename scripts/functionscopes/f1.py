# names declared in a function are local to function
# i.e. they cannot be used outside the function.
def funct(y):
    x = 1
    print(x,y )
    
funct(10)
print(x,y)