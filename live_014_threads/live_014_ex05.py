import threading
from time import sleep

def wait():
    count = 0
    while True:
        print(count)
        count += 1
        sleep(0.1)

t = threading.Thread(target=wait, name='Wait')
t.start()
print(threading.enumerate()[1].is_alive())
sleep(1)
print(t.is_alive())
