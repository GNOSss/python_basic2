#__call__(self, ...)

class Soldier:
    def __init__(self, rank, name):
        self.rank = rank
        self.name = name

    def __call__(self):
        print(f"{self.rank} {self.name}!")


soldier_1 = Soldier("이병", "김돌준")
soldier_2 = Soldier("상병", "유린기")

soldier_1()
soldier_2()