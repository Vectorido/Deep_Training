# Classic factorial
def fact_old(n):
    pr = 1
    a = []
    for i in range(1, n + 1):
        pr = pr * i
        a.append(pr)
    return a

def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr = pr * i
        yield pr

s = fact(10)

for i in s:
    print(i, end=' ')