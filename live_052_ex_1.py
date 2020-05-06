from threading import Event
from queue import Queue
from urllib.parse import urljoin
from requests import get

base_url = 'http://pokeapi.co/api/v2/'
event = Event()
fila = Queue(maxsize=101)


def get_urls():
    pokemons = get(urljoin(base_url, 'pokemon/?limit=5')).json()['results']
    import ipdb; ipdb.set_trace()

get_urls()


# Comandos digitados no terminal
# $ python ex_1a.py
# ipdb> pokemons
# ipdb> fila
# ipdb> fila.queue
# ipdb> pokemons[0]
# ipdb> fila.put(pokemons[0])
# ipdb> fila.queue
