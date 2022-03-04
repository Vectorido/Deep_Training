class Person:
    def __init__(self, name, surname, gender='male'):
        if gender != ('male', 'female'):
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            gender = 'male'
        self.name = name
        self.surname = surname
        self.gender = gender

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'