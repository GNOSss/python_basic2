# 프로그래밍에서 함수는 크게 두 가지의 의미를 갖습니다.
# 1. 반복될 수 있는 작업을 정의
# 2. input을 받아 output을 반환

# 1. 기본 사용법
# -작업을 함수로 지정
# def my_func():
# - 컨벤션 : 함수명도 스네이크 케이스로 명명
# - 어떤 일을 하는지 나타낼 것
#     print("반복 될 수 있는")
#     print("일정 규모의 작업")
# 함수 정의부 아래는 2줄 이상을 띄울 것 (스타일 가이드)


# my_func() #이렇게 함수명을 입력하면 작동함


# def mult_5_and_print(x):  # x: 매개변수
#     print(x * 5)
#
#
# mult_5_and_print(3)  # 3: 인자
# mult_5_and_print("하")  # "하": 인자
#
# def add_and_print(x, y):
#     print(x + y)
#
#
# add_and_print(2, 3)