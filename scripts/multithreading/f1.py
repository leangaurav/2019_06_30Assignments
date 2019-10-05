import threading

print(dir(threading))
t = threading.current_thread()
print(t)

print(dir(t))