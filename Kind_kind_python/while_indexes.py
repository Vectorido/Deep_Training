p = [0] * 10

while True:
    n = int(input())
    if p.count(1) == 5:
        break
    if p[n] == 1:
        continue
    p[n] = 1

print(p)
