class Progression:
    def __init__(self, n):
        self.n = n  # amount of elements
        self.a = 2
        self.d = 3

    def summa(self):
        if self.n <= 0:
            raise ValueError
        s = (self.n * (2 * self.a + self.d * (self.n - 1))) / 2
        return s


def main():
    progression = Progression(25)  # create progression where first element=1, difference=3,amount of elements=10
    print('sum => {summa}'.format(summa=progression.summa()))


if __name__ == '__main__':
    main()
