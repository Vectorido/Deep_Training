class MoneyBox:
    def __init__(self, capacity):
        self.value = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.value + v < self.capacity
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        self.value += v
        return self.value
        # положить v монет в копилку


##### Переопределение классов #####

class Person:
    name = 'Adam'

    def __init__(self, name):
        print('init Person')
        self.name = name

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек ходит')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()

    def __str__(self):
        return f'Doctor {self.name}'


class Doctor(Person):
    def breathe(self):
        print('Доктор дышит')

    # def __str__(self):
    # return f'Doctor {self.name}'


# d = Doctor('John')
# p = Person('Adam')
# p.combo()
# d.combo()
# print(p, d)

##### Наследование классов. Расширение. Extending #####

class Person:
    age = 100

    def sleep(self):
        print('Человек спит')

    def combo(self):
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()
        if hasattr(self, 'age'):
            print(self.age)
        pass


class Doctor(Person):
    age = 30

    def sleep(self):
        print('Доктор спит')

    def walk(self):
        print('Доктор ходит')


# p = Person()
# d = Doctor()
# p.combo()
# d.combo()

##### Наследование. Делегирование. Delegating #####


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def info(self):
        print('parent class')
        print(self)


class Doctor(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor {self.name}, {self.surname}'


p = Person('Ivan', 'Ivanov')
d = Doctor('Petr', 'Petrov', 25)

#print(d.name, d.surname, d.age)
#d.info()

##### Множественное наследование классов #####

class Doctor:

    def can_cure(self):
        return f'Doctor '

class Builder:

    def can_build(self):
        return f'Builder'