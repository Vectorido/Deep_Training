import sys, numpy as np

# считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
lst_in = [[1, 0, 0, 0, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 0, 1]]

a = np.array(lst_in)
a = np.pad(a, 1, mode='constant')

for i in range(1, len(a) - 1):
    for j in range(1, len(a[i]) - 1):
        if a[i][j] == 1:
            if any([a[i][j + 1] == 1,
                   a[i + 1][j] == 1,
                   a[i + 1][j + 1] == 1,
                   a[i + 1][j - 1] == 1]):
                print('НЕТ')
                break
    else:
        continue
    break
else:
    print('ДА')

# print('ДА' if flag else 'НЕТ')