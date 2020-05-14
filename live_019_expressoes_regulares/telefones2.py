import re
from itertools import permutations
from time import sleep

cel = re.compile(r'[7-9][0-9]{8}')

for tel in permutations(range(10), 9):
    _tel = ''.join(str(x) for x in tel)
    if cel.search(_tel):
        print('11-' + _tel)
