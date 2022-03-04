class NewInt(int):

    def repeat(self, n=2):
        return int(str(self) * n)

    @property
    def to_bin(self):
        return int(f'{self:b}')

