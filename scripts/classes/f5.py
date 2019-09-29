class Test:
    def __new__(clas, *args, **kwargs):
        obj = super().__new__(clas)
        print('New', obj)
        return obj
        
    def __init__(self, a):
        print('Init', a, self)
        
t1 = Test(1)
t2 = Test(2)