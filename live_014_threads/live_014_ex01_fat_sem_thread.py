from time import time

numbers = [2139079, 124759, 1516637, 1852285]

def factorize(number):
    for i in range(1, number + 1):
        if number % 1 == 0:
            yield i

start = time()
for number in numbers:
    list(factorize(number))
end = time()

print(f'{end-start}')
