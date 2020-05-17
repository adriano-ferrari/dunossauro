import threading

print(threading.active_count())
print(threading.enumerate())
print(threading.enumerate()[0].name)
print(threading.enumerate()[0].is_alive())

