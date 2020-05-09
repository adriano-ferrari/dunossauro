"""Exemplo de Pool nativo."""
from multiprocessing import Pool
#from multiprocessing.dummy import Pool
from os import getpid
from pprint import pprint

def soma_2(x):
    return x + 2, getpid()

workers = Pool(5)


# syn
result = workers.map_async(soma_2, range(100))
pprint(result)

# syn
result = workers.map_async(soma_2, range(100))
pprint('bananas')
result.wait()
pprint('bananas2')
pprint(result.get())
