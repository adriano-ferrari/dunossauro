"""Exemplo de como compartilhar uma queue entre processos e threads."""
from threading import Thread
from os import getpid, getppid

