# Borgh Singleton: different objects, shared state
class Test:
    __d = {}
    
    def __new__(clas, *args, **kwargs):
        obj = super().__new__(clas)
        obj.__dict__ = Test.__d
        return obj
        
    def __init__(self):
        print('Init', self)
        
t1 = Test()
t2 = Test()
print(id(t1),id(t2)) 
print(id(t1.__dict__), id(t2.__dict__))
t1.x = 100
t2.x = 200
t2.y =4000
print(t1.x, t1.y)
