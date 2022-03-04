a, b = int(input()), int(input())
c = a * b
# fastest algorithm for 'НОД'

while b > 0:
    a, b = b, a % b
    # c = a % b
    # b = c

print(a)

# algorith for 'НОК'

NOK = int(c / a)

print(NOK)
