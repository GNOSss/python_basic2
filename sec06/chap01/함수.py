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


# #함수 사용후 반환값 얻어내기
# def add(x, y):
#     print(f"{x}와 {y}를 더합니다.")
#     return x + y
#
#
# add_1 = add(2, 3)
# add_2 = add("안녕", "하세요")
#
# # add함수안에 add함수가 2개 존재함 총 3번의 add함수를 실행하게 됨
# add_3 = add(add(2, 3), add(4, 5))
#
# pass

# - `return` 연산자는 뒤의 값을 반환하며 **함수를 종료**
#     - 가장 마지막에 작성할 것
# - 값을 반환하는 함수는 그 실행부를 반환값으로 “바꿔 쓸 수 있음”
# def add(x, y):
#     print(f"{x}와 {y}를 더합니다.")
#     return x + y
#
# add_1 = add(2, 3)
# add_2 = add("안녕", "하세요")
#
# add_3 = add(add(2, 3), add(4, 5))


# 주어진 리스트 중 정수만 골라 총합, 개수, 평균 반환
# def get_stats(lst):
#
#     total = 0
#     item_count = 0
#
#     for item in lst:
#         if not isinstance(item, int):
#             continue
#         total += item
#         item_count += 1
#     average = total / item_count
#
#     # 튜플로 반환
#     return item_count, total, average
#
#
# my_list = [1, 2, "가", 3, 3.14, 4, (1, 2), 5, "Hello"]
# #return의 3가지 값을 언패킹해서 묶어줌 !!! 내가 잘 안써본거라 응용해보기
# l_count, l_total, l_avg = get_stats(my_list)
#
# print(l_count)
# print(l_total)
# print(l_avg)
# pass

# # 주어진 리스트 중 정수만 골라 총합, 개수, 평균 반환
# def classify_by_type(items):
#     # 결과를 저장할 딕셔너리 초기화
#     type_dict = {}
#
#     # 리스트의 모든 요소를 순회
#     for item in items:
#         # 현재 요소의 타입을 얻기
#         item_type = type(item).__name__
#
#         # 해당 타입의 키가 딕셔너리에 없으면 새 리스트로 초기화
#         # type_dict에 item_type 이 없다면 (ex. type_dict에 int형이 없다면..)
#         if item_type not in type_dict:
#             #type_dict[int]=[] 이렇게 생성하라는 것
#             type_dict[item_type] = []
#
#         # 현재 요소를 올바른 타입 리스트에 추가
#         type_dict[item_type].append(item)
#
#     # 분류된 딕셔너리 반환
#     return type_dict
#
#
# # 함수 사용 예
# example_list = [1, 2, "hello", 3.14, "world", True, [1, 2, 3], {"a": 1}, (4, 5)]
# classified_dict = classify_by_type(example_list)
# print(classified_dict)
