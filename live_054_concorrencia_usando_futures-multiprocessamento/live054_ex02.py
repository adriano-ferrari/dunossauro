from concurrent.futures import ThreadPoolExecutor
from time import sleep


with ThreadPoolExecutor(max_workers=3) as exe:
    result_0 = exe.submit(sleep, 10)
    result_1 = exe.submit(print, 'oi')
    print(result_0)
    print(result_1)
