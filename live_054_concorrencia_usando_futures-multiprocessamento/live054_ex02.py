from concurrent.futures import ThreadPoolExecutor
from time import sleep


with ThreadPoolExecutor(max_workers=1) as exe:
    """
    GIL: tarefas bloqueantes de I/O.

    Darão bypass no GIL
    """
    result_0 = exe.submit(sleep, 10)
    result_1 = exe.submit(print, 'oi')
    print(result_0)
    print(result_1)
