#상속은 한 클래스의 속성과 메소드를 다른 클래스가 물려받게 하는 것으로,
#코드의 재사용성을 늘리고 연관된 클래스들의 관계를 구축하는데 사용됩니다.
class YalcoChicken:
    company_name = "얄코치킨"
    next_no = 1

    def __init__(self, name):
        self.no = YalcoChicken.next_no
        self.name = name
        YalcoChicken.next_no += 1

        # 매장마다 메뉴가 바뀔 수 있으므로 인스턴스 속성으로
        self.chicken_menus = {
            "양념": {"price": 12_000, "spicy": True},
            "후라이드": {"price": 10_000, "spicy": False}
        }

    def order_chicken(self, chicken_name):
        chicken_menu = self.chicken_menus.get(chicken_name)
        if chicken_menu:
            return f"{chicken_name}은(는) {chicken_menu['price']}원입니다."
        else:
            return "그런 치킨은 없습니다."

    def intro(self):
        return f"안녕하세요, {YalcoChicken.company_name} {self.no}호 {self.name}점입니다!"


store_1 = YalcoChicken("강남")
store_1_order_1 = store_1.order_chicken("양념")
store_1_order_2 = store_1.order_chicken("간장")





class YalcoChickenPub(YalcoChicken):
    sub_comp_name = "얄코치킨 & 펍"

    def __init__(self, name):
        # super() : 부모 클래스를 가리킴
        # 부모 클래스의 생성자 먼저 실행
        super().__init__(name)
        self.drink_menus = {
            "맥주": {"price": 3000},
            "소주": {"price": 2000},
        }

    def order(self, chicken_name, drink_name):
        # 부모 클래스의 메소드 실행
        result = super().order_chicken(chicken_name)

        drink_menu = self.drink_menus.get(drink_name)
        if drink_menu:
            result += f"{drink_name}은(는) {drink_menu['price']}원입니다."
        else:
            result += " 그런 음료는 없습니다."
        return result

    # 부모의 메소드 오버라이드
    def intro(self):
        return f"안녕하세요, {YalcoChickenPub.sub_comp_name} {self.no}호 {self.name}점입니다!"

# next_no(클래스 변수)는 부모와 같은 값 사용 확인
store_2 = YalcoChickenPub("신촌")
store_3 = YalcoChickenPub("명동")

store_2_order_1 = store_2.order("양념", "맥주")

# 자식 클래스는 부모의 메소드 호출 가능 (반대는 성립 X)
store_2_order_2 = store_2.order_chicken("후라이드")

store_1_intro = store_1.intro()
# 오버라이드 override : 부모의 메소드를 덮어쓰기
store_2_intro = store_2.intro()


# 자식 클래스의 인스턴스는 부모 클래스에 속함
is_inst_1 = isinstance(store_2, YalcoChickenPub)
is_inst_2 = isinstance(store_2, YalcoChicken)
# 반대는 성립하지 않음
is_inst_3 = isinstance(store_1, YalcoChickenPub)

pass