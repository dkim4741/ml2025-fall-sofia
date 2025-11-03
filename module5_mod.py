class NumberCollection:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def find_index(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1