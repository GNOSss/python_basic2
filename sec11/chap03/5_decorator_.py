def conditional_execution(is_enabled):
    def decorator(func):
        #주목 !! *args, **kwargs 는 꼭 (@,@)의 형태의 매개변수를 받을 필요가 없음
        #어떠한 형태가 와도 매개변수로 받는다는 일종의 선언임
        def wrapper(*args, **kwargs):
            if is_enabled:  #if is_enabled: 가 True 이면 return func(*args,**kwargs) 한다는 뜻
                return func(*args, **kwargs)
            else:
                print(f"⚠️ {func.__name__} : 조건불충족")
        return wrapper
    return decorator

## option_num = 1 이고 @conditional_execution(option_num%2)는 True로 반환됨

option_num = 1
# option_num += 1

@conditional_execution(option_num % 2) # 💡 함수 실행부 형태임 주목
def when_odd():
    print("홀수일 때 실행")


@conditional_execution(not option_num % 2)
def when_even():
    print("짝수일 때 실행")


when_odd()
when_even()