s = input().replace(" ", "")
a = []
count = ""
for i in s:
    if i.isdigit():
        count += i
    elif i == "-":
        a.append(count)
        count = ""
        count += i
    elif i == "+":
        a.append(count)
        count = ""
    else:
        a.append(count)
        count = ""
        a.append(i)
a.append(count)
print(sum(map(int, a)))