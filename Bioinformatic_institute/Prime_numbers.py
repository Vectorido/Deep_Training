import itertools

def primes():
    prime = True
    i = 1
    while True:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                prime = False
        if prime:
            yield i
        else:
            prime = True

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
