def f1():
    x = 10
    def f2():
        x = 20
        print(x)
    print("Before f2: ", x)
    f2()
    print("After f2:  ",x)
    
def f11():
    x = 10
    def f22():
        nonlocal x # brings the name from nearest outer non-global scope into current scope
        x = 20
        print(x)
    print("Before f2: ", x)
    f22()
    print("After f2:  ",x)
    
    
f1()

print('Second Change')
f11()