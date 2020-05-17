from threading import Timer
from time import sleep

var = True

def hello():
    global var
    print('hello timer')
    var = False

t = Timer(2, hello)
t.start()

while var:
    print('hello')
    sleep(0.3)
