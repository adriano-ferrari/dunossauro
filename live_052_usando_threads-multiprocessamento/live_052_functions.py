from contextlib import contextmanager
from datetime import datetime
from shutil import copyfileobj, rmtree
from requests import get
from os import makedirs
from os.path import exists

path = 'download_live_052'
if exists(path):
    rmtree(path)
makedirs(path)

def get_bin_file(args):
    """Faz o download do binário."""
    name, url = args
    return name, get(url, stream=True).raw


def get_sprite_url(url, sprite='front_default'):
    """Pega a url do sprite."""
    return url['name'], get(url['url']).json()['sprites'][sprite]


def save_file(args, path=path, type_='png'):
    """Salva o binário no disco como imagem."""
    name, binary = args
    fname = f'{path}/{name}.{type_}'
    with open(fname, 'wb') as f:
        copyfileobj(binary, f)
    return fname

def pipeline(*funcs):
    def inner(argument):
        state = argument
        for func in funcs:
            state= func(state)
    return inner


target = pipeline(get_sprite_url, get_bin_file, save_file)

@contextmanager
def timeit(*args):
    start_time = datetime.now()
    yield
    time_elapsed = datetime.now() - start_time
    print(f'Total tempo (hh:mm:ss.ms) {time_elapsed}')
