# 모든 인터페이스를 위한 부모 클래스
class Interface:
    dark_mode_on = False  # 모든 인스턴스에 공통적으로 적용되는 다크 모드 속성

    def __init__(self, size):
        self.size = size  # 인터페이스의 크기

    def click(self):
        print("클릭")

    @classmethod
    def toggle_dark_mode(cls):
        cls.dark_mode_on = not cls.dark_mode_on
        print("다크 모드:", "켜짐" if cls.dark_mode_on else "꺼짐")

# 일반 버튼 클래스
class Button(Interface):
    def __init__(self, size, label):
        super().__init__(size)
        self.label = label  # 버튼의 각인

    def click(self):
        print(f"{self.label} 클릭")

# 토글 버튼 클래스
class ToggleButton(Interface):
    def __init__(self, size, is_on=False):
        super().__init__(size)
        self.is_on = is_on  # 토글 상태

    def click(self):
        self.is_on = not self.is_on
        print("토글 버튼 상태:", "켜짐" if self.is_on else "꺼짐")

# 드롭다운 메뉴 클래스
class DropdownMenu(Interface):
    def __init__(self, size, options):
        super().__init__(size)
        self.options = options  # 드롭다운 메뉴의 옵션들

    def click(self):
        print("드롭다운 메뉴 옵션:")
        for option in self.options:
            print(option)

    def choose_menu(self, choice):
        if choice in self.options:
            print(f"선택된 메뉴: {choice}")
        else:
            print("잘못된 선택")

# 인스턴스 생성 및 사용 예
button = Button(10, "확인 버튼")
button.click()

toggle_button = ToggleButton(10)
toggle_button.click()  # 토글 상태 변경
toggle_button.click()  # 다시 토글

dropdown_menu = DropdownMenu(15, ["옵션 1", "옵션 2", "옵션 3"])
dropdown_menu.click()
dropdown_menu.choose_menu("옵션 2")

Interface.toggle_dark_mode()  # 다크 모드 토글
