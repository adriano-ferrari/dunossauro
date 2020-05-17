from threading import Timer

def hello():
    print('hello timer')

t = Timer(5, hello)
t.start()

