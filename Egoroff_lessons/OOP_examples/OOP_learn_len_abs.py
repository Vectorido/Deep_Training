class Distance:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self) #self.__abs__()

    def __abs__(self):
        return abs(self.x2 - self.x1)

