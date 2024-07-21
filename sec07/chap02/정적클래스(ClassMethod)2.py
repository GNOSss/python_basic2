class YalcoChicken:
    company_name = "얄코치킨"
    # 다음에 오픈할 매장의 번호
    next_no = 1

    def __init__(self, name):
        self.no = YalcoChicken.next_no
        self.name = name
        YalcoChicken.next_no += 1

    def intro(self):
        return f"안녕하세요, {YalcoChicken.company_name} {self.no}호 {self.name}점입니다!"

store_1 = YalcoChicken("강남")
store_2 = YalcoChicken("판교")
store_3 = YalcoChicken("제주")

store_1_intro = store_1.intro()
store_2_intro = store_2.intro()
store_3_intro = store_3.intro()

pass