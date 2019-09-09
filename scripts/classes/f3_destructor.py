class Test:
    def __init__(self, id):
        self.id = id
        print('init', id)
    def __del__(self):
        print('del id :', self.id)
        
def test_funct():
    t = Test(100)
    print('in function')

t1 = Test(10)
t2 = Test(20)

test_funct()

del t2
print('Some text')