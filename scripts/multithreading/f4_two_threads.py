import threading

def funct(id, count):
    for i in range(count):
        print(id, i)
    
t1 = threading.Thread(target = funct, args = ('T1', 50))
t1.start()

t2 = threading.Thread(target = funct, args = ('T2', 50))
t2.start()

for t in threading.enumerate():
    if t.name != 'MainThread':
        t.join()

print('Main', threading.current_thread())  