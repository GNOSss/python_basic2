import functools


def logger(func):
    # 함수의 매개변수들 사용
    def wrapper(*args, **kwargs):
        print(f"✏️ {func.__name__} 함수 호출 - 인자: {args}, {kwargs}")
        # func.__name__은 def arith 함수 명 , {args}는 def func 함수의 인자 x,y의 값을 ,  {kwargs}는 def func 함수의 키워드 인자 func = lambda x,y : 를 출력함
        return func(*args, **kwargs)
    return wrapper


@logger
def arith(x, y, *, func):
    return func(x, y)


arith(3, 4, func=lambda x, y: x + y)
arith(10, 20, func=lambda x, y: x * y)