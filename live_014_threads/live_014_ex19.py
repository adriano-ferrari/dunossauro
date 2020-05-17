from threading import Thread

c = 0

def count_300():
    global c
    while c < 3000:
        c += 1
    print(c)

def count_1000():
    global c
    c = 3001
    while c < 10000:
        c += 1
    print(c)

t_0 = Thread(target=count_300, name='300', daemon=True)


t_1 = Thread(target=count_1000, name='1000')
t_1.start()
t_0.start()

count_300()
count_1000()
