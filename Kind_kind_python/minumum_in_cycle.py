n = list(map(float, input().split()))

minimum = n[0]

for i in n:
    if i < minimum:
        i = minimum

print(minimum)
