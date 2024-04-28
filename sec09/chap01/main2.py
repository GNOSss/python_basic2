class YalcoChicken:
    company_name = "얄코치킨"
    # 다음에 오픈할 매장의 번호
    next_no = 1

    def __init__(self, name):
        self._no = YalcoChicken.next_no
        self.name = name
        YalcoChicken.next_no += 1

    def intro(self):
        return f"안녕하세요, {YalcoChicken.company_name} {self.no}호 {self.name}점입니다!"

    @property
    def no(self):
        return str(self._no) + "번 매장"

    @no.setter
    def no(self, value):
        raise AttributeError("매장 번호는 바꾸지 않습니다.")
        # Error는 이후 배울 것


store_1 = YalcoChicken("강남")
store_2 = YalcoChicken("판교")

store_1_no = store_1._no
store_2_no_a = store_2.no

# 💡 오류를 발생시킴
# store_2.no = 3

# 속성에 직접 접근하여 바꾸는 것은 막지 못함
# store_2._no = 3
# store_2_no_c = store_2.no


pass