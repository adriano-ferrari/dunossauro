"""Exemplo de como compartilhar uma queue entre processos e threads."""
from collections import namedtuple
from threading import Thread
from os import getpid, getppid

pstate = namedtuple('psstate', 'name pid ppid')


def info(name):
    obj = pstate(name, getpid(), getppid())
    print(obj)


print(info('main line'))
