def decorator(func):
    def inner(n, m):
        print('start decorator...')
        func(n, m)
        print('finish decorator...')

    return inner


def say(name, surname):
    print('hello', name, surname)


#
# say = decorator(say)
# say('Vasya', 'Ivanov')
#
# print(say)


def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


@table
@header
def say(name, surname):
    print('hello', name, surname)


say('Vasya', 'Ivanov')
