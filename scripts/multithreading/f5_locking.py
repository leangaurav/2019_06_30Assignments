import threading

counter = 0

def funct(id, count):
    global counter
    for i in range(count):
        counter += 1
        #print(id, counter)
    
t1 = threading.Thread(target = funct, args = ('T1', 100000))
t1.start()


t2 = threading.Thread(target = funct, args = ('T2', 100000))
t2.start()

for t in threading.enumerate():
    if t.name != 'MainThread':
        t.join()

print('Main', counter)  