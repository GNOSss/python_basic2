class FibonacciIter:
    def __init__(self, count):
        self.count = count
        self.num1, self.num2 = 0, 1
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count >= self.count:
            raise StopIteration

        if self.current_count == 0:
            self.current_count += 1
            return self.num1
        elif self.current_count == 1:
            self.current_count += 1
            return self.num2
        else:
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current_count += 1
            return self.num2


numbers = list(FibonacciIter(10))

pass