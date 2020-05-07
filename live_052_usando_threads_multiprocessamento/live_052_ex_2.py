from threading import Event
from queue import Queue
from urllib.parse import urljoin
from requests import get

base_url = 'http://pokeapi.co/api/v2/'
event = Event()
fila = Queue(maxsize=101)


def get_urls():
    pokemons = get(urljoin(base_url, 'pokemon/?limit=5')).json()['results']
    [fila.put(pokemon) for pokemon in pokemons]
    import ipdb; ipdb.set_trace()

get_urls()


# Comandos digitados no terminal
# $ ipython ex_1b.py
# ipdb> fila.queue
# ipdb> fila.get()
# ipdb> fila.queue
