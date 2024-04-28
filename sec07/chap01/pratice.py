class YalcoChiken:
    def __init__(self, no, name):
        self.no = no
        self.name = name

    def intro(self):
        return print(f"안녕하세요. 얄코치킨 {self.no}호 {self.name}점입니다.")

store_1 = YalcoChiken(1,"강남")
stroe_2 = YalcoChiken(2,"판교")

print(store_1.intro())
