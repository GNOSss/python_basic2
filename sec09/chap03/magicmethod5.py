class StickSet:
    def __init__(self, number, length):
        self.number = number
        self.length = length

    def __len__(self):
        return self.number * self.length


ss_1 = StickSet(50, 3)
ss_2 = StickSet(35, 6)

#len으로 __len__메소드를 호출할 수 있음
ss_1_len = len(ss_1)
ss_2_len = len(ss_2)

pass