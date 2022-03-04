from math import factorial as fact


def factorial(n: int):
    return fact(n)
    pass


def trailing_zeros(n: int) -> str:
    a = str(factorial(n))
    return str(len(a) - len(a.rstrip('0')))
    pass


# print(factorial(5))

#print(trailing_zeros(20))

MIN_DRIVING_AGE = 18


def allowed_driving(name, age: int):
    print(f'{name} еще рано садиться за руль' if age < MIN_DRIVING_AGE else f'{name} может водить')
    "здесь напишите свой код"


# allowed_driving('tim', 18)


def print_goods(*args):
    out = [v for v in args if isinstance(v, str) and v]
    if out:
        for i, v in enumerate(out, 1):
            print(f'{i}. {v}')
    else:
        print('Нет товаров')


#print_goods(1, True, '')


def info_kwargs(**kwargs):
    for i in sorted(kwargs):
        print(f'{i} = {kwargs[i]}')


info_kwargs(first_name="John", last_name="Doe", age=33)
