#객체 지향 프로그래밍 디자인 패턴의 하나로,
#특정 클래스의 인스턴스가  프로그램 전체에서 하나만 존재해야 할 때 사용합니다.

class Theme:
    def __init__(self, dark_mode=False):
        self.dark_mode = dark_mode

class Tab:
    def __init__(self, name):
        self.name = name
        self.theme = Theme()  # 각 탭마다 새로운 Theme 인스턴스 생성


#tab_1, tab_2에 각각 Theme라는 클래스형식의 인스턴스를 각각 같고 있음
#tab_1.theme.dark_mode = True 를 통해서 tab_1의 정보(속성)를 변경할 수 있다는 것

tab_1 = Tab("Home")
tab_2 = Tab("Profile")

tab_1_is_dark_a = tab_1.theme.dark_mode
tab_2_is_dark_a = tab_2.theme.dark_mode

tab_1.theme.dark_mode = True

tab_1_is_dark_b = tab_1.theme.dark_mode
tab_2_is_dark_b = tab_2.theme.dark_mode

pass