##### Множественное наследование классов #####

class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Ура, я отучился на доктора')

    def can_cure(self):
        return f'Doctor'

    def can_build(self):
        return f'Doctor_B'


class Builder:
    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print('Ура, я отучился на строителя')

    def can_build(self):
        return f'Builder'


class Person(Builder, Doctor):
    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self, degree)

    def __str__(self):
        return f'Person {self.rank} {self.degree}'


print(Person.__mro__)
s = Person(5, 'spec')
print(s)