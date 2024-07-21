#인스턴스가 각 매장이라면 클래스는 본사입니다.
#이번 강에서 배우는 요소들은 본사가 갖고 있고 모든 매장들에 동일하게 적용되는 요소들입니다.
class YalcoChicken:
    # 클래스 변수
    company_name = "얄코치킨"

    # 클래스 메소드
    #- `@classmethod` 로 명시
    #- 첫 인자로 해당 클래스를 가리키는 `cls` 받음 cls 가 곧 클래스를 가리킴
    #- 클래스의 상태에 접근하고 관련된 작업을 할 수 있음
    #- 클래스와 인스턴스에서 모두 사용 가능
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name


    # 정적 메소드
    # - @ staticmethod로 명시
    # - 클래스의 상태와 무관한 메소드
    # - 클래스와 인스턴스에서 모두 접근 가능
    @staticmethod
    def tax_investigation():
        return "세무자료"


    def __init__(self, no, name):
        self.no = no
        self.name = name

    def intro(self):
        return f"안녕하세요, {YalcoChicken.company_name} {self.no}호 {self.name}점입니다!"
#인스턴스 속성들은 각 매장마다 따로 있지만 클래스 변수는 본사 한 곳에만 위치합니다.


# 클래스 변수는 인스턴스 메소드에서 사용 가능 (반대는 동작X)
store_1 = YalcoChicken(1, "강남")
store_1_intro = store_1.intro()

# 클래스 변수는 클래스에서 접근 가능 (인스턴스에서도 가능)
yc_company_name = YalcoChicken.company_name

# @classmethod의 메소드 def change_company_name 을 호출하여 newname에다가 "얄코순대국밥"을 넘겨줌
YalcoChicken.change_company_name("얄코순대국밥")
store_1.change_company_name("얄코순대국밥")
yc_new_company_name = YalcoChicken.company_name
store_1_new_intro = store_1.intro()

# 정적 메소드도 클래스에서 접근 가능 (인스턴스에서도 가능)
tax_invest_result = YalcoChicken.tax_investigation()








pass