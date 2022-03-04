from timeit import timeit


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Point(3, 4)

print(s.__sizeof__(), s.__dict__.__sizeof__())


def make_c11():
    s = Point(3, 4)
    s.x = 100
    s.x
    del s.x


def make_c12():
    s = PointSlots(3, 4)
    s.x = 100
    s.x
    del s.x


# print(timeit(make_c11))
# print(timeit(make_c12))

class Rectangle:
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter call')
        self.__width = value


class Square(Rectangle):
    __slots__ = tuple()
    def __init__(self, a, b):
        super().__init__(a, b)

c = Rectangle(10, 50)
c._Rectangle__width  # Вызов защищенной переменной
