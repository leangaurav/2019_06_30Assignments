import time, threading

a = []
e = threading.Event()

def producer(name):
    for i in range(100):
        a.append(i)
        e.set()# signal an event
        print(name,'produced', i)
        time.sleep(0.01)
    
    a.append(None) 
    e.set()# signal an event

def consumer(name):
    while True:
        e.wait()# blocking call
        e.clear()
        
        if len(a) != 0:
            data = a.pop()
            print(name, 'consumed', data)
            
            if data == None:
                a.append(None) # multiple consumers
                e.set()# signal an event
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