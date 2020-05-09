from concurrent.futures import ThreadPoolExecutor


with ThreadPoolExecutor(max_workers=3) as exe:
    result_1 = exe.submit(print, 'oi')
    print(result_1)
