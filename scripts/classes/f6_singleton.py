# Singleton : Design Pattern : you have only one instance/ copy of a class
# you can create only one object of a class

class Test:
    __instance = None
    
    def __new__(clas, *args, **kwargs):
        if Test.__instance == None:
            Test.__instance = super().__new__(clas)
        return Test.__instance
        
    def __init__(self):
        print('Init', self)
        
t1 = Test()
t2 = Test()
t2 = Test()
t2 = Test()
t1.x = 100
t2.x = 200
print(t1.x)