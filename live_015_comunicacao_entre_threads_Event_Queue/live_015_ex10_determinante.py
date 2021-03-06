from threading import Thread
from queue import Queue
from time import sleep
from functools import reduce

q = Queue(maxsize=2)
r = Queue()

matriz = [[2, 9],
          [-1, 6]]


def principal(mat):
    sleep(10)
    q.put(mat[0][0] * mat[1][1])


def secundaria(mat):
    count = 0
    while q.empty():
        count += 1

    print(count)
    q.put(mat[1][0] * mat[0][1])


def result():
    count = 0
    while not q.full():
        count += 1

    print('result', count)
    r.put(reduce(lambda x, y: x - y, q.queue))


t_p = Thread(target=principal, kwargs={'mat': matriz}, name='Principal')
t_p.start()

t_s = Thread(target=secundaria, kwargs={'mat': matriz}, name='Secudária')
t_s.start()

t_r = Thread(target=result, name='result')
t_r.start()
t_r.join()

print(r.queue[0])
