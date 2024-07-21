#주어진 값에 따라 다양한 동작을 지정할 수 있습니다. 타 언어의 switch 문과 유사하나 차이점이 있습니다.
# #타 언어 `switch` 문과의 차이
# - 패턴 매칭 사용 가능
# - `break` 문 없음

person = "Alice"

match person:
    case "Alice":
        print("엘리스 안녕! 잘 지냈니? 밥은 먹었어?")
    case "Bob":
        print("왔냐")
    case _:
        print("어서오세요.")
# - `case _` : 위의 `case` 들 중 어느 곳에도 속하지 않는 값일 때
#     - 맨 마지막에 사용

x = 0
y = 5

match x:
    case 0:
        print("Case A")
    case  1 | 2 | 3:  # 1,2,3 중에 하나의 값이 있다면 "Case B" 출력
        print("Case B")
    case 4 if x < y: # x의 값이 4이면 y의 값보다 작으면 "Case C" 출력
        print("Case C")
    case _ if x > y: #위의 Case에 해당되지 않고 if문에 True이면 "Case D"출력
        print("Case D")
    case _:
        print("Case E")


var = True
# `bool()` 을 `int()` 보다 위에 둘 것
# - `bool`은 `int`의 한 종류이므로, `int()` 가 위에 있으면 `True` 와 `False` 가 그곳에 매칭됨
match var:
    case bool():
        print("불리언입니다.")
    case int():
        print("정수입니다.")
    case float():
        print("실수입니다.")
    case str():
        print("문자열입니다.")
    case _:
        print("기타 자료형입니다.")

# my_list = []
# my_list = ["apple"]
# my_list = ["apple", "banana"]
my_list = ["apple", "banana", "orange", "mango"]

match my_list:
    case []:
        print("빈 리스트")
    case [s]:
        print(f"한 요소: {s}")
    case [s, c]:
        print(f"두 요소: {s}, {c}")
    case [s, *rest]: # 💡 이후 이터러블 배운 뒤 다시 살펴볼 것
        print(f"첫 요소: {s}, 나머지: {rest}")

# point = (0, 0)
# point = (2, 0)
point = (0, 3)
# point = (4, 5)
# point = 1

match point:
    case (0, 0):
        print("원점")
    case (x, 0):
        print(f"X={x}")
    case (0, y):
        print(f"Y={y}")
    case (x, y):
        print(f"X={x}, Y={y})")
    case _:
        print("좌표가 아닙니다.")

# my_dict = {}
# my_dict = {"name": "홍길동", "age": 30}
# my_dict = {"school": "엄석대", "major": "컴퓨터공학"}
my_dict = {"job": "개발자", "position": "팀장", "years": "5"}

match my_dict:
    case {"name": name, "age": age}:
        print(f"인적 정보 - {name}({age})세")
    case {"school": school, "major": major}:
        print(f"학력 정보 - {school} 졸업 ({major} 전공)")
    case {"job": job, **rest}: # 이터러블 배운 뒤 다시 살펴볼 것
        print(f"직업 정보 - {job}")
    case {}:
        print("빈 딕셔너리")