class Vector:
    def __init__(self, *args):
        self.values = sorted([arg for arg in args if isinstance(arg, int)])

    def __str__(self):
        if len(self.values):
            return f'Вектор{tuple(self.values)}'
        else:
            return f'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*[i + other.values[self.values.index(i)] for i in self.values])
            else:
                print('Сложение векторов разной длины недопустимо')
        elif isinstance(other, int):
            return Vector(*[i + other for i in self.values])
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*[i * other.values[self.values.index(i)] for i in self.values])
            else:
                print('Умножение векторов разной длины недопустимо')
        elif isinstance(other, int):
            return Vector(*[i * other for i in self.values])
        else:
            print(f'Вектор нельзя умножать с {other}')
