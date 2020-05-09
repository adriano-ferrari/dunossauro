from urllib.parse import urljoin
from multiprocessing import Pool
from requests import get
from live053_functions import target, timeit

base_url = 'https://pokeapi.co/api/v2/'


def get_urls():
    """Faz o get das urls."""
    return get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']


with timeit():
    poke = get_urls()
    with Pool(15) as workers:
        result = workers.map(target, poke)
        result2 = workers.map(target, poke)
    print(result)
    print(result2)
