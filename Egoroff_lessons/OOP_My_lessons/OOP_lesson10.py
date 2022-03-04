# class City:
#
#     def __init__(self, name):
#         city = name.lower().split()
#         for i in range(len(city)):
#             city[i] = city[i][0].upper() + city[i][1:]
#         self.city = ' '.join(city)
#
#     def __str__(self):
#         return self.city
#
#     def __bool__(self):
#         return self.city[-1].lower() not in 'aoeiu'


class Quadrilateral:

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def __str__(self):
        if self.width == self.height:
            return f'Куб размером {self.width}x{self.height}'
        return f'Прямоугольник размером {self.width}x{self.height}'

    def __bool__(self):
        return self.width == self.height
