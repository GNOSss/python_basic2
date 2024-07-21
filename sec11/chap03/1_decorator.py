# 데코레이터
# 파이썬에서 데코레이터는 다른 함수를 수정하지 않고 기능을 추가하거나 변경할 수 있는 강력한 도구입니다.
# 데코레이터는 함수를 인자로 받아 다른 함수를 반환하는 함수입니다

# 데코레이터의 구조와 적용 방식
# 1. 데코레이터 함수 정의
# 2. 데코레이터 내부에 또 다른 함수(내부 함수)를 정의
# 3. 내부 함수에서 외부 함수의 인자로 받은 함수를 호출
# 4. 내부 함수를 반환
# 5. 외부 함수에 **`@`** 심볼을 이용하여 다른 함수에 적용


# 1.
def my_decorator(func):
    # 2.
    def wrapper():
        print("함수 실행 전")
        func() # 3.
        print("함수 실행 후")
    return wrapper #4.

# 데코레이터(@my_decorator)로 추가한 def say_hello() 는 위 def my_decorator(func)의 func로 인자로 받게 됨
# 그래서 def wrapper() 내장함수의 func()로 호출하게 됨
@my_decorator # 5.
def say_hello():
    print("안녕하세요!")


say_hello()



