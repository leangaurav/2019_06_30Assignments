import threading

def funct(id, count):
    for i in range(count):
        print(id, i)
    
t1 = threading.Thread(target = funct, args = ('T1', 50))
t1.start()

print('Main')  