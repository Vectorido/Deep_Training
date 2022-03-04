class Buffer:
    def __init__(self):
        self.ls = []

    def add(self, *args):
        for i in args:
            self.ls.append(i)
            if len(self.ls) == 5:
                print(sum(self.ls))
                self.ls = []

    def get_current_part(self):
        return self.ls