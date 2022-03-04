def pretty_print(data, side='-', delimiter='|'):
    symb = 0
    for i in data:
        symb += len(str(i))
    print(symb)
    print(f' {side * (symb + len(data) * 2 + 2)}')
    for i in data:
        print(f'{delimiter} {i} ', end = '')
    print(f'{delimiter}')
    print(f' {side * (symb + len(data) * 2 + 2)}')

pretty_print([455466, 749, 84, 1, 1, 1, 1])


