class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.pos = 0;
        self.neg = 0;
        self.i = 0
        self.n = len(iterable)
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __next__(self):
        while True:
            if self.i < self.n:
                for f in self.funcs:
                    if f(self.iterable[self.i]):
                        self.pos += 1
                    else:
                        self.neg += 1

                if self.judge(self.pos, self.neg):
                    self.pos = 0
                    self.neg = 0
                    res = self.i
                    self.i += 1
                    return res
                self.i += 1
                self.pos = 0
                self.neg = 0
            else:
                raise StopIteration

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self


l = MyList([1, 2, 3, 4, 5])
for i in l:
    print(i)
