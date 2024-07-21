#클로저
#둘러싼 스코프의 변수값을 기억하는 함수입니다.
#값을 은닉하거나 고차함수를 생성하는데 사용됩니다.

def make_counter():
    count = 0 # 반환될 함수에 의해 기억될 값
# count 변수는 make_counter의 실행이 끝나면 메모리에서 제거되어야 함
    #그러나 이를 사용하는 내부 함수(def counter)가 외부로 반환(return counter)되어 , 그 안에 기억됨
        #외부에서 접근하여 살펴볼 수 없는 형태로 은닉됨
    def counter():
        nonlocal count # 💡 쉐도잉하지 않도록
        count += 1
        return count
    return counter


counter_1 = make_counter()

for _ in range(5):
    print(counter_1())

count_now = counter_1()


# 새로 만든 카운터는 별개의 값들 반환
counter_2 = make_counter()
c2_counts = [counter_2() for i in range(10)]

pass