class multifilter:
    def judge_half(pos, neg):
        return pos >= neg  # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return pos >= 1  # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0  # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.lst = iterable  # iterable - исходная последовательность
        self.funcs = funcs  # funcs - допускающие функции
        self.judge = judge  # judge - решающая функция

    def __iter__(self):
        for el in self.lst:
            pos, neg = 0, 0
            for f in self.funcs:
                pass
                if f(el):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield el


# Examples of filters

def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))