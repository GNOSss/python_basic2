#main.py은 tab 1,2가 각각 따로 놀게 끔 되어있다
#main2.py는 tab 1,2의 Theme가 같이 돌아가게끔 설정할 수 있음

# 구분                       __new__                                                    __init__
# 역할                객체(인스턴스) 생성                                객체(인스턴스) 초기화
# 타입                   클래스 메소드                                                인스턴스 메소드
# 사용 시점  객체가 메모리에 생성될 때 호출        __new__로 생성된 객체를 초기화할 때 호출
# 첫 번째 인자     클래스 자체 (cls)                            인스턴스 자체 (self)
# 반환값         새로 생성된 인스턴스                         None (반환값이 있으면 안 됨)
# 호출 방식   object의 __new__를 명시적으로 호출 필요 (super().__new__(cls, ...))    객체 생성시 파이썬이 자동으로 호출

#__init__은 클래스 인스턴스를 통해서 들어오면 매번 생성자를 초기화해서 만듦 즉 메모리가 계속 생성
#__new__는 super().__new__(cls, ...)) 호출문이 필요하고 생성된 인스턴스를 추가로 못만들게 함
#__new__는 클래스 메소드임 , cls는 클래스 자체를 말함


class Theme:
    #프로그램 전체에서 단 하나만 존재하는 인스턴스 _instance
    _instance = None


#__new__메소드 : 인스턴스 생성 과정을 커스터마이징할 때 사용

    def __new__(cls, dark_mode=False):
        if cls._instance is None:
            cls._instance = super(Theme, cls).__new__(cls)
            cls._instance.dark_mode = dark_mode
        return cls._instance

class Tab:
    def __init__(self, name):
        self.name = name
        self.theme = Theme()  # 모든 탭에서 동일한 Theme 인스턴스 공유


tab_1 = Tab("Home") #tab_1 으로 호출시 __new__를 통해 Theme인스턴스 생성완료
tab_2 = Tab("Profile") #tab_2 호출시 이미 tab_1으로 생성된 인스턴스가 있어 그걸로 반환됨

tab_1_is_dark_a = tab_1.theme.dark_mode
tab_2_is_dark_a = tab_2.theme.dark_mode

tab_1.theme.dark_mode = True

tab_1_is_dark_b = tab_1.theme.dark_mode
tab_2_is_dark_b = tab_2.theme.dark_mode

pass