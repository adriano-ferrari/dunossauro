import threading
from time import sleep

def wait():
    sleep(2)



t1 = threading.Thread(target=wait, name='Wait', daemon=True)
t1.start()
print(t1.is_alive())
print(t1.name)


t2 = threading.Thread(target=wait, name='Wait')
t2.start()
print(t2.is_alive())
print(t2.name)
