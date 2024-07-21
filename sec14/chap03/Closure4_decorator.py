# 💡 데코레이터에서 이미 사용한 바 있음

def my_decorator(func):
    def wrapper():
        print("함수 실행 전")
        func()                      # say_hello()를 호출하게 되면 func을 감싸고 있는 def wrapper()도 같이 실행됨
        print("함수 실행 후")
    return wrapper #4.


@my_decorator
def say_hello():        # def say_hello() 가 my_decorator의 func으로 들어가게 됨
    print("안녕하세요!")


say_hello()

#위 코드에서 my_decorator는 say_hello 함수를 데코레이트합니다.
# 데코레이터는 다른 함수를 감싸는 역할을 하며, 함수 실행 전후에 특정 동작을 추가할 수 있습니다.
# 여기서 wrapper 함수가 say_hello 함수를 감싸고, say_hello 함수 실행 전후에 메시지를 출력합니다.
# 코드를 단계별로 살펴보겠습니다:
# my_decorator 함수는 func라는 인수를 받습니다.
# my_decorator 함수 안에 wrapper라는 내부 함수를 정의합니다. 이 함수는 func를 호출하기 전과 후에 메시지를 출력합니다.
# wrapper 함수를 반환하여 데코레이터로 사용됩니다.
# @my_decorator는 say_hello 함수를 데코레이트하여 say_hello가 wrapper 함수로 대체되도록 합니다.
# say_hello()를 호출하면 실제로 wrapper 함수가 호출되어 메시지가 출력되고, 그 안에서 func()가 호출되면서 원래의 say_hello 함수가 실행됩니다.