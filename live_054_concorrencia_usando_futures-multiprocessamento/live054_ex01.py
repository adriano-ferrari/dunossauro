from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from requests import get


l_urls = ['https://google.com'] * 6

# executor = ThreadPoolExecutor(max_workers=3)
# result = executor.map(get, l_urls)
# print(list(result))

with ThreadPoolExecutor(max_workers=3) as executor:
    """
    executor.__enter__ -> self (ThreadPoolExecutor)
    executor.__exit__ -> executor.shutdown (wait= True)
    """
    result = executor.map(get, l_urls)
    print(result)
