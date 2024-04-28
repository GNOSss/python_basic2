class YalcoChicken:
    # 클래스 변수
    company_name = "얄코치킨"

    def change_company_name(cls, new_name):
        cls.company_name = new_name

    def __init__(self, no, name):
        self.no = no
        self.name = name

    def intro(self):
        return f"안녕하세요, {YalcoChicken.company_name} {self.no}호 {self.name}점입니다!"

store_1 = YalcoChicken(1, "강남")
store_1_intro = store_1.intro()

# 클래스 변수는 클래스에서 접근 가능 (인스턴스에서도 가능)
yc_company_name = YalcoChicken.company_name

YalcoChicken.change_company_name("얄코순대국밥")
yc_new_company_name = YalcoChicken.company_name
store_1_new_intro = store_1.intro()