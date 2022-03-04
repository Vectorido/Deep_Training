m, y, w, x = [sorted(list(map(int,input().split()))) for i in range(4)]
for i in y:
    for j in x:
        if abs(i - j) <= 1:
            x.remove(j)
            #print(x)
print(w[0] - len(x))