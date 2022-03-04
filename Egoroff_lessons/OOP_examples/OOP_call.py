##### ПОЛИМОРФИЗМ POLYMORPHISM #####

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle'

    def get_area(self):  ## Названия функций/методов должны совпадать
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Square'

    def get_area(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Circle'

    def get_area(self):
        return 3.14 * self.r ** 2


##### Magic method __call__ #####


class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('__init__ object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'наш экземпляр вызывался {self.counter} раз')

    def average(self):
        return self.summa / self.length


from time import perf_counter


class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Вызывалась функция {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Функция отработала за {finish - start}')
        return result


@Timer
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

##### Magic method __getitem__, __setitem__, __delitem__ #####

class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Индекс за гранью')

    def __setitem__(self, key, value):
        if 0 < key < len(self.values):
            self.values[key] = value
        elif key >= len(self.values):
            diff = key - len(self.values) + 1
            self.values.extend([0] * diff)
            self.values[key] = value
        else:
            raise IndexError('Индекс за гранью')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за гранью')


##### Magic method __iter__, __next__ #####

class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

    def __iter__(self):
        print('call iter')
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        print('call next marks')
        if self.index > len(self.marks) - 1:
            raise StopIteration
        letter = self.marks[self.index]
        self.index += 1
        return letter

class Mark:
    def __init__(self, values):
        self.value = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('call next marks')
        if self.index > len(self.value) - 1:
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter

m = Mark([3, 4, 5, 6, 7])

igor = Student('Igor', 'Nikolaev', m)
for i in igor:
    print(i, end = ' ')