import threading

lck = threading.Lock()

counter = 0

def funct(id, count):
    global counter
    for i in range(count):
        with lck: # blocking call: passes only when lock in not locked
            counter += 1
    
t1 = threading.Thread(target = funct, args = ('T1', 100000))
t1.start()

t2 = threading.Thread(target = funct, args = ('T2', 100000))
t2.start()

t3 = threading.Thread(target = funct, args = ('T3', 100000))
t3.start()

for t in threading.enumerate():
    if t.name != 'MainThread':
        t.join()

print('Main', counter)  