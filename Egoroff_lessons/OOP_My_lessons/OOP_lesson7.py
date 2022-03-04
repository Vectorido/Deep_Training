class Vector:
    def __init__(self, *args):
        values = []
        for i in args:
            if type(i) == int:
                values.append(i)
        self.values = values

    def __str__(self):
        if len(self.values):
            return f'Вектор {tuple(sorted(self.values))}'
        else:
            return f'Пустой вектор'
