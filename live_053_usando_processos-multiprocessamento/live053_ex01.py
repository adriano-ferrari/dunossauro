"""Exemplo de como compartilhar uma queue entre processos e threads."""
from threading import Thread
from os import getpid, getppid

def info(name):
    print(name, getpid(), getppid())


print(info('main line'))
