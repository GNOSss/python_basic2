# 이터레이터는 다음 차례 값을 반환하는 __next__() 메소드를 가지며
# iter() 호출시 스스로를 반환합니다.

class CounterIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# 이터레이터 사용
counter = CounterIterator(1, 7)

# 이터레이터를 반복하면서 값을 얻기
# def __next__ 호출
value_0 = next(counter)
value_1 = next(counter)
value_2 = next(counter)

# 이미 진행한 이후는 나머지 값들만
# 즉 위 value_0 ~ 2 까지는 1,2,3을 각각 나타내고
# for number in counter 는 나머지 값 4,5,6,7을 반환함
for number in counter:
    print(number)


# 때문에 재사용시 다시 생성하여 사용할 것
for number in CounterIterator(1, 5):
    print(number)


# iter가 스스로를 반환
counter_iter = iter(counter)
counter_is_iter = counter is counter_iter


# 컴프리헨션
numbers = [num for num in CounterIterator(1, 5)]


# 언패킹 적용
*rest, second_last, last = list(CounterIterator(1, 7))
#second_last, last 는 int 형태로 저장되어 있음



#이터레이터 만들기 실습 (주어진 회수 만큼 주사위를 굴리는 이터레이터)

import random

class DiceIterator:
    def __init__(self, rolls):
        self.rolls = rolls
        self.current_roll = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_roll >= self.rolls:
            raise StopIteration
        self.current_roll += 1
        return random.randint(1, 6)


# roll 변수에 이터레이터 클래스 호출 5번 굴린 결과값 출력
for roll in DiceIterator(5):
    print(roll)

# 컴프리헨션를 응용
rolls_1 = ["🎲 " + str(roll) for roll in DiceIterator(5)]
rolls_2 = ["🎲 " + str(roll) for roll in DiceIterator(5)]

# 클래스 호출 후 언패킹하여 각각 나눠서 담음
first, second, third, *rest = list(DiceIterator(5))


pass