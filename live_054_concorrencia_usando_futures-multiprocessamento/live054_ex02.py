from concurrent.futures import ProcessPoolExecutor
from time import sleep


with ProcessPoolExecutor() as exe:
    """
    GIL: tarefas bloqueantes de I/O.

    Darão bypass no GIL
    """
    result_0 = exe.submit(sleep, 10)
    result_1 = exe.submit(print, 'oi')
    print(result_0)
    print(result_1)
