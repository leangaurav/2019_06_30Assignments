import time, threading

a = []

def producer(name):
    for i in range(100):
        a.append(i)
        print(name,'produced', i)
        time.sleep(0.05)
    
    a.append(None) 

def consumer(name):
    while True:
        while len(a) == 0:# busy waiting
            pass
        data = a.pop()
        print(name, 'consumed', data)
        
        if data == None:
            a.append(None) # multiple consumers
            break
        
t1 = threading.Thread(target = producer, args = ('P1', ))
t1.start()

t2 = threading.Thread(target = consumer, args = ('C1', ))
t2.start()

t3 = threading.Thread(target = consumer, args = ('C2', ))
t3.start()

for t in threading.enumerate():
    if t.name != 'MainThread':
        t.join()
        
print(a)