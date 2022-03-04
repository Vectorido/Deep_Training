n = int(input())

money = [64, 32, 16, 8, 4, 2, 1]

while n > 0:
    # for i in range(len(money)):
    for i in money:
        if n < i:
            money.remove(i)
        else:
            n -= i
            print(i)
            break
