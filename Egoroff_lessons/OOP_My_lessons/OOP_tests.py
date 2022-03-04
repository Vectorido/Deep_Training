class SoccerPlayer():
    def __init__(self, name='', surname=''):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0
    def score(self, score=1):
        self.goals += score
    def make_assist(self, make_assist=1):
        self.assists += make_assist
    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
