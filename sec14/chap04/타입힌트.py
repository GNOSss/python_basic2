# 타입힌트
# 변수, 매개변수, 반환값 등의 자료형을 명시하여 가독성을 높이고 오용을 줄일 수 있습니다.
# 'IDE의 힌트 기능에 활용될 수 있습니다. 단, 언어에 의해 강제되지는 않습니다.

# 아래처럼 변수명:자료형식 = 값을 넣어도 문제는 없음
age: int = 25
name: str = "Alice"
scores: list = [90, 80, 70, 60]
# 그러나 아래 변수명들이 이미 다른 유형으로 정의되어 오류를 야기할 수 있음을 밑줄로 표시해줌
# age = "26"
# scores = 90


# multiply 함수의 매개변수의 유형을 설명할 수 있고 , 반환값의 유형도 설명해줄 수 있음
# 명심할 것은 def multiply(x: float, y: float) -> str: 이렇게 쓴다고 str형식으로 반환되는게 아님
def multiply(x: float, y: float) -> str:
    return f"{x} * {y} = {x * y}"
    # return x * y

aa = multiply(3,4)
print(aa)
print(type(aa))




# names:list[str] , 반환값이 None 이라고 명시해줌으로써
# 매개 변수값들과 return문의 유무에 대해서 오류를 야기할 수 있음을 표시해줄 수 있음
def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello", name)
    # return f"Hello {name}"


greet_all(["Alice", "Bob", "Charlie"])
# greet_all("Alice")
# greet_all([1, 2, 3, 4, 5])





from typing import Optional
import random


# 💡 값이 None일 수도 있을 때
def money_or_none() -> Optional[str]:
    luck = random.randint(0, 1)
    return "💰" if luck else None
    # return "💰"
    # return None
    # return 123