class Test:
    x = 10 # Class Attribute: shared by all objects
    y = 'string'
  
    def __init__(self, a):
        self.abc = a
        print('init')
        
t1 = Test(10)
t2 = Test(20)

print(t1.abc)
print(t2.abc)

print()
print(Test.x)
print(t1.x)
print(t2.x)

print()
t1.y = 'pqr'
print(Test.y)
print(t1.y)
print(t2.y)