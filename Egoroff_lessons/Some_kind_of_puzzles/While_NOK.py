def NOD(a, b):
    while b:
        a, b = b, a % b
    return a


def NOK(a, b):
    return a * b // NOD(a, b)


print(NOK(*map(int, input().split())))
