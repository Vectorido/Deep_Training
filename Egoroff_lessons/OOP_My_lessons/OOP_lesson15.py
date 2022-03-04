class Wallet:

    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError('Неверный тип валюты')
        elif len(list(currency)) != 3:
            raise NameError('Неверная длина названия валюты')
        elif currency.upper() != currency:
            raise ValueError('Название должно состоять только из заглавных букв')
        else:
            self.currency = currency
            self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        if self.currency != other.currency:
            raise ValueError('Нельзя сравнить разные валюты')
        else:
            return self.balance == other.balance

    def __add__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError('Данная операция запрещена')
        else:
            new_balance = self.balance + other.balance
            return Wallet(self.currency, new_balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError('Данная операция запрещена')
        else:
            new_balance = self.balance - other.balance
            return Wallet(self.currency, new_balance)


