import time, threading
from queue import Queue

a = Queue() # FIFO

def producer(name):
    for i in range(100):
        a.put(i) # signals
        print(name,'produced', i)
        time.sleep(0.01)
    
    a.put(None) 
    
def consumer(name):
    while True:
        data = a.get()# blocking call
        
        print(name, 'consumed', data)
            
        if data == None:
            a.put(None)
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
        
print(a.qsize())