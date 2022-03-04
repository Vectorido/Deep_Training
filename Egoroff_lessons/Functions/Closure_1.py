def main_func(value):
    name = value

    def inner_func():
        print('hello my friend', name)

    return inner_func()


main_func('s')


def adder(value):
    def inner(a):
        return value + a

    return inner


print(adder(5)(5))


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


print(counter())