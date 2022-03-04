import functools


def mod_checker(x, mod=0):
    return lambda y: y % x == mod



mod_3 = mod_checker(3)


print(mod_3(4))


mod_3_1 = mod_checker(3, 1)

print(mod_3_1(4)) # True
s = 's'
from math import pi
print(f"Значение числа pi: {pi:.2f}")

print(s.startswith.__doc__)