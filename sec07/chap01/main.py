# 클래스 정의
# 메소드 : 어떠한 클래스에 속한 함수 !!!!
# 클래스명 짓는 규칙? : 첫글짜는 대문자  ex) AppleBanana
# class YalcoChicken:
#     # 생성자 (constructor)
#     def __init__(self, no, name):
#         # 인스턴스 속성 (instance attribute)
#         self.no = no
#         self.name = name
#
#     # 인스턴스 메소드
#     def intro(self):
#         return f"안녕하세요, 얄코치킨 {self.no}호 {self.name}점입니다!"
#
# #함수처러 아래에 두 줄 공백 남김 (스타일 가이드)
# #인스턴스 instance 는 다른 강좌나 책에서 객체 object 라고도 불림
# #위 맥락의 속성 attribute 은 변수라 불리기도 함
#
# # 인스턴스 생성 (생성자 호출)
# store_1 = YalcoChicken(1, "강남")
# store_2 = YalcoChicken(2, "판교")
#
# # 인스턴스가 클래스에 속하는지 확인
# store_type = type(store_1).__name__ # 💡 인스턴스가 속한 클래스의 이름을 반환
# store_is_yc = isinstance(store_1, YalcoChicken)
#
# # 인스턴스 메소드 호출
# store_1_intro = store_1.intro()
# store_2_intro = store_2.intro()



# class Button:
#     def __init__(self, imprint, spaces):
#         self.imprint = imprint
#         self.spaces = spaces
#
#     def place(self):
#         print(f"각인: {self.imprint}, 칸 수: {self.spaces}")
#
#
# buttons = [
#     Button("0", 2),
#     Button("1", 1),
#     Button("=", 3)
# ]
#
# for button in buttons:
#     button.place()



class Slime:
    def __init__(self):
        self.hp = 50.0
        self.attack = 8.0
        self.defense = 0.2

    def attack_enemy(self, enemy):
        print("💥 퍽!")
        enemy.hp -= self.attack * (1 - enemy.defense)


slime_1 = Slime()
slime_2 = Slime()

#def attack_enemy 메소드에 enemy매개변수에 slime_2를 넘겨줌
slime_1.attack_enemy(slime_2)

#def attack_enemy 메소드에 enemy매개변수에 slime_1를 넘겨 hp가 0이 될때까지 실행
while slime_1.hp > 0:
    slime_2.attack_enemy(slime_1)

pass