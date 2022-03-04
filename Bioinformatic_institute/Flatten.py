# Функция для преобразования вложенных списков в один общий

def flatten(enlim):
    if len(enlim) == 1:
        if type(enlim[0]) == list:
            result = flatten(enlim[0])
        else:
            result = enlim
    elif type(enlim[0]) == list:
        result = flatten(enlim[0]) + flatten(enlim[1:])
    else:
        result = [enlim[0]] + flatten(enlim[1:])
    return result


print(flatten([1, [2, 3, [4]], 5]))