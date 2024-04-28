# #매개변수
# #기본값을 가진 매개변수
# # 💡 기본값 매개변수는 뒤쪽에 있어야 함 (바꿔 볼 것)
# def make_coffee(cup, type="아메리카노"):
#     return f"{type} {cup}잔 준비되었습니다."
#
#
# # 기본값 매개변수 사용
# #매개변수가 1개여도 오류 발생 안됨 def make_coffee 함수에 "아메리카노"변수로 적용되서 반환됨
# #단 기본값이 없는 매개변수는 기본값이 있는 매개변수 뒤에 가면 안됨
# coffee_result = make_coffee(2)
# coffee_result_latte = make_coffee(1, "라떼")
# coffee_result_moca = make_coffee(1,"모카")
# pass

# 정해지지 않은 수의 매개변수 튜플로 받기
# def 함수명( * 매개변수):
# def add_numbers(*numbers):
#     print(numbers, type(numbers).__name__)
#     total = 0
#     for number in numbers:
#         total += number
#     return total
#
#
# result = add_numbers(1, 2, 3, 4, 5)
#
# pass


#키워드 매개변수
#실행부에 매개변수의 이름을 적어 인자의 대상 특정
#이를 적지 않고 매개변수의 순서를 기준으로 하는 것은 위치 매개변수라고 함
#매개변수에 자료값만 있으면 순서영향이 있지만 키워드와 매개변수를 같이 사용해서 순서상관없음
#대신 호출함수에서 매개변수 전달시 키워드가 중복으로 되면 안됨
# def create_profile(name, age, job):
#     return f"이름: {name}, 나이: {age}, 직업: {job}"
#
# # 키워드 매개변수 사용
# prof_1 = create_profile(name="지훈", age=30, job="개발자")
#
# # 키워드 매개변수는 순서를 바꾸어도 정상 작동
# prof_2 = create_profile(job="디자이너", age=25, name="수민")
#
# # 일부만 키워드 매개변수로 사용 가능
# prof_3 = create_profile("영희", job="교사", age=28)

# ⚠️ 위치 매개변수는 앞쪽의 것을 사용해야 함
# prof_4 = create_profile("개발자", name="돌준", age=22)

# 💡 * 뒤로 오는 매개변수는 키워드 전용
# def create_user(name, age, *, email, phone=None):
#     user_info = {
#         "name": name,
#         "age": age,
#         "email": email,
#         "phone": phone
#     }
#     return user_info
#
# # 키워드 전용 매개변수는 반드시 키워드로 호출
# user1 = create_user("김철수", 30, email="kcs@***.com")
# user2 = create_user("이영희", 25, email="lyh@***.com", phone="123-4567")
#
# # ⚠️ 어길 시 오류 발생
# # user3 = create_user("박돌준", 27, "pdj@***.com", "234-5678")
#
# pass

# # 모든 매개변수가 키워드 전용
# def calculate_area(*, width, height):
#     return width * height
#
# # 이렇게하면 오류남
# # test1 = calculate_area((3,4))
# # 이렇게하면 오류 안남
# test2 = calculate_area(width=3, height=4)

# #가변 키워드 매개변수
# def build_profile(**info):
#     info_type = type(info).__name__
#     return info # 🔴
#
#
# profile_result = build_profile(name="지훈", age=30, job="개발자")
#

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# print_info(name="John", age=30, city="New York")
#
# #
# # 일반 매개변수와 함께 사용
# def create_user_profile(username, email, **additional_info):
#     profile = {
#         "username": username,
#         "email": email
#     }
#     for key, value in additional_info.items():
#         profile[key] = value
#     return profile
#
#
# user_profile = create_user_profile(
#     "김철수", "kcs@***.com",
#     age=30, location="Seoul", phone="010-1234-5678"
# )
#
#
# # *args에 위치 매개변수(걍 자료들) * kwargs에 키워드 매개변수가 들어가게 됨
# def print_args_and_kwargs(*args, **kwargs):
#     print(f"위치 인자들: {args}")
#     for arg in args:
#         print(arg)
#
#     print(f"\n키워드 인자들: {kwargs}")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# print_args_and_kwargs('apple', 'banana', 'cherry', name='김돌준', age=30, country='대한민국')
#

