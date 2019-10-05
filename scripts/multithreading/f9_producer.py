import time, threading

a = []

def producer(name):
    for i in range(10):
        a.append(i)
        print(name,'produced', i)
        time.sleep(0.1)
    
        

def consumer(name):
    while len(a) > 0:
        data = a.pop()
        print(name, 'consumed', data)
        
t1 = threading.Thread(target = producer, args = ('P1', ))
t1.start()

t2 = threading.Thread(target = consumer, args = ('C1', ))
t2.start()

for t in threading.enumerate():
    if t.name != 'MainThread':
        t.join()
        
print(a)