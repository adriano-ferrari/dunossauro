from threading import Event, Thread
from time import sleep


def wait_set():
    sleep(3)
    event.set()


event = Event()
t = Thread(target=wait_set)
t.start()

print('antes')
event.wait()
print('depois')
event.clear()
t.start()
event.wait()
print('depois depois')
