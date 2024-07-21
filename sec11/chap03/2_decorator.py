
import time


def timer(func):
    def wrapper(*args, **kwargs): # 함수에 어떤 매개변수가 사용되는지 모르므로
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏲️ {func.__name__} 실행 시간: {end_time - start_time}초")
        return result
    return wrapper


@timer
def exp_func():
    total = 0
    for i in range(1, 10000000):
        total += (i * i - i) / i
    return total


exp_func()