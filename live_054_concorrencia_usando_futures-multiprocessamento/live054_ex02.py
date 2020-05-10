from concurrent.futures import ProcessPoolExecutor
from time import sleep
from functools import partial


with ProcessPoolExecutor() as exe:
    """
    GIL: tarefas bloqueantes de I/O.

    Darão bypass no GIL
    """
    result_0 = exe.submit(sleep, 5)
    result_1 = exe.submit(print, 'oi')
    print(result_0)
    print(result_1)
    result_0.add_done_callback(partial(print, 'acabei'))
