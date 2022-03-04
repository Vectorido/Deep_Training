class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        elif isinstance(other, (int, float)):
            return self.rating == other
        else:
            print('Невозможно выполнить сравнение')

    def __gt__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        elif isinstance(other, (int, float)):
            return self.rating > other
        else:
            print('Невозможно выполнить сравнение')

    def __lt__(self, other):
        if not isinstance(other, (ChessPlayer, int, float)):
            print('Невозможно выполнить сравнение')

