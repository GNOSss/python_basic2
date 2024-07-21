def cache_decorator(func):
    # 메모리 한 곳에 위치한 딕셔너리
    # 즉 cache = {} 는 중복 실행을 방지하는 인자값과 반환값을 저장함
    # cache = {}에는 print(expensive_function(10000)) , 이것에 10000을 키 값으로 저장과 10000으로 실행한
    # 반환값을 딕셔너리 형태로 저장
    cache = {}

    def wrapper(*args, **kwargs):
        # 캐시에 해당 매개변수를 키로 하는 요소가 있으면
        if args in cache:
            return cache[args]  # return - 함수를 종료
            # cache = {} 는 딕셔너리 형태로 데이터를 저장하기 때문에
            # 이미 갖고있는 값을 호출 할때 cache[args] 대로 작성하여 반환한다.
        # 없다면 함수 실행
        result = func(*args, **kwargs)
        # 캐시에 저장
        cache[args] = result
        return result

    return wrapper


@cache_decorator
def expensive_function(num):
    print(f"{num} 계산중...")
    return sum(i * i for i in range(num))


# 함수 호출
print(expensive_function(10000))
print(expensive_function(10000))

print(expensive_function(20000))

