from threading import Event, Thread
from queue import Queue
from urllib.parse import urljoin
from requests import get
from time import sleep
from live_052_functions import target, timeit

base_url = 'http://pokeapi.co/api/v2/'
event = Event()
fila = Queue(maxsize=101)


def get_urls():
    pokemons = get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']
    [fila.put(pokemon) for pokemon in pokemons]
    event.set()
    fila.put('Kill')


class Worker(Thread):
    def __init__(self, target, queue, *, name='Worker'):
        super().__init__()
        self.name = name
        self.queue = queue
        self._target = target
        self_stoped = False
        print(self.name, 'started')

    def run(self):
        event.wait()
        while not self.queue.empty():
            pokemon = self.queue.get()
            print(self.name, pokemon)
            if pokemon == 'Kill':
                self.queue.put(pokemon)
                self._stoped = True
                break
            self._target(pokemon)

    def join(self):
        while not self._stoped:
            sleep(0.1)

with timeit():
    get_urls()
    print(fila.queue)
    print('start')
    th = Worker(target=target, queue=fila, name='Worker1')
    th2 = Worker(target=target, queue=fila, name='Worker2')
    th2 = Worker(target=target, queue=fila, name='Worker3')
    print('starts')
    th.start()
    th2.start()
    th3.start()
    print('joins')
    th.join()
    th2.join()
    th3.join()


# Comandos digitados no terminal
# $ python ex_1d.py
# ipdb> pokemons[0]
# ipdb> get(pokemons[0]['url']).json()
# ipdb> xpto = get(pokemons[0]['url']).json()
# ipdb> xpto['sprites']
