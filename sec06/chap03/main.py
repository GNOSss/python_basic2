#함수의 중첩
#함수 안에 다른 함수가 정의되는 것

# result_1 이 outer_function 을 호출
# # outer_function이 return으로 inner_function을 호출함
# def outer_function(outer_arg):
#     # 외부 함수
#
#     def inner_function(inner_arg):
#         # 내부 함수 - 스코프가 외부함수 내로 제한됨
#         return inner_arg * 2
#
#     return inner_function(outer_arg)
#
#
# result_1 = outer_function(5)
# # result_2 = inner_function(5) # ⚠️ 오류
#
# pass


#스코프
#변수, 함수, 객체 등이 "유요한"(접근 가능한) 범위
# def outer_function():
#     in_outer = 1 # inner_function 함수에서도 사용가능
#
#     def inner_function():
#         in_inner = 2
#         print(in_outer)
#         print(in_inner) #inner_function함수에서만 제한있게 사용가능
#
#     inner_function()
#
#     print(in_outer)
#     # print(in_inner) # ⚠️
#
#
# outer_function()

# print(in_outer) # ⚠️ #in_outer는 def outer_fucntion함수에서만 사용 가능함
# print(in_inner) # ⚠️ #in_inner는 def inner_function함수에서만 사용 가능함

# for문의 경우는 스코프 적용이 다름
#루프가 시작되는 스코프는 하나의 전역 스코프로 본다.ㄴ
# for i in range(3):
#     for j in range(3):
#         print(f"안쪽 {i} {j}")
#     print(f"중간 {i} {j}")
#
# print(f"바깥 {i} {j}")


#쉐도잉
#바깥쪽 스코프의 변수가 안쪽 스코프의 동명 변수에 의해 가려짐
# def outer_scope():
#     king = "사자"
#     lord = "늑대"
#     print(f"바깥: {king} {lord}")
#
#     def middle_scope():
#         king = "여우"
#         print(f"중간: {king} {lord}")
#
#         def inner_scope():
#             king = "고양이"
#             lord = "쥐"
#             print(f"안쪽: {king} {lord}")
#
#         inner_scope()
#
#     middle_scope()
#
#
# outer_scope()

# 쉐도잉 예제2 inner()함수의 x가 outer()함수의 x를 덮어버리지만
# inner()함수가 종료되면 다시 x가 outer()함수의 x로 적용 된다.
# 그러나 nonlocal x 를 해버리면 outer()함수의 x값이 변경된다.
# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x  # 💡 바깥의 x를 그대로 사용
#         x = "nonlocal"
#         print("inner:", x)
#
#     inner()
#     print("outer:", x)
#
#
# outer()


#쉐도잉 예제3
#my_function()함수에서 global x 를 선언하는 의미는
# 바깥라인에 x = 0 을 x = 10으로 변경한다는 의미
# 만약 global x 선언이 없으면 x = 0으로 출력된다.
# x = 0  # 전역 변수
#
# def my_function():
#     global x  # 💡 전역의 x를 그대로 사용
#     x = 10
#
# my_function()
# print(x)


#재귀함수 : 함수가 자기 자신을 호출하여 실행
# 카운트다운
def countdown(n):
    if n <= 0:
        print("카운트다운 종료!")
    else:
        print(n)
        countdown(n - 1)


countdown(5)


# 팩토리얼
#호출 매개변수 5 는  n으로 대입된다. 조건문에 else에 해당되기때문에
# 5 * 4 * 3 * 2 까지하고 마지막 n == 1에 해당 누적된 return연산과 합산되어
# 최종 120으로 출력됨
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))


# 피보나치
# # 피라미드 형식으로 값이 전달되니 그림 해석이 필요함
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(10))



