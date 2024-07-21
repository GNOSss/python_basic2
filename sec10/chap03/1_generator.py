# 제너레이터는 특별한 종류의 이터레이터로서,
# 이터레이터를 생성하기 위한 간편하고 메모리 효율적인 방법을 제공합니다.

from collections.abc import Iterator


# 간단한 제너레이터 함수 정의
def simple_generator():
    yield 1
    yield 2
    yield 3
#- `yield` 를 만날 때마다 뒤의 값을 반환 후 멈춤 (해당 상태가 저장됨)
#    - `next()` 가 직관적으로 구현된 모습

# 제너레이터 함수 사용
gen = simple_generator()
gen_type = type(gen).__name__

# 이터레이터의 일종임 확인
gen_is_iter = isinstance(gen, Iterator)


# 첫 번째 값 가져오기
first_value = next(gen)

# 남은 값들을 순회하기
for value in gen:
    print(value)  # 2, 3 순서로 출력될 것임




#  sec10의 chap02의 이터레이터를 제너레이터로 만들기
# class CounterIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1


def counter_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

for number in counter_generator(1, 5):
    print(number)

numbers = list(counter_generator(1, 5))




pass