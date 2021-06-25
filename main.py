num = [1, 2, 3, 4, 5, 6]
s = ('A', 'B', 'C', 'D')
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
z = set([1, 2, 3, 4, 1])
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 10:
        print(n)
    else:
        break



    

















