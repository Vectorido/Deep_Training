#Разбиение по уровням

def rec(ls, level=1):
    print(*ls, 'level=' + str(level))
    for i in ls:
        if type(i) == list:
            rec(i, level+1)

a = [1, 2, [2, 3, 4, [3, 4, [2, 3], 5]]]

rec(a)
