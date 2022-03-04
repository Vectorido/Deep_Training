class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if not isinstance(value, int) or value < 0:
            print('Error dollars')
        else:
            self.total_cents = value * 100 + self.total_cents % 100

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if not isinstance(value, int) or value < 0 or value >= 100:
            print('Error cents')
        else:
            self.total_cents = value + (self.total_cents // 100) * 100

    def __str__(self):
        return f'Ваше состояние составляет {self.total_cents // 100} долларов {self.total_cents % 100} центов'
