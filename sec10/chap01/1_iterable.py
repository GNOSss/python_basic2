# 프로그래밍에서 이터러블(iterable)이란 리스트, 튜플, 셋 딕셔너리, 문자열처럼
# 포함된 요소들을 하나하나 돌아가면서 처리하거나 반환할 수 있는 객체를 말합니다.
# 파이썬에서 for … in 루프를 사용할 수 있는 객체들은 이터러블이라고 말할 수 있습니다.


# 💡 이터레이터(다음 강에 배움)를 반환
str_is_iterable = iter("Hello")
list_is_iterable = iter([1, 2, 3])
tuple_is_iterable = iter((True, False))
set_is_iterable = iter({"A", "B", "C"})
dic_is_iterable = iter({"pi": 3.14})


class MyClass:
    pass


# ⚠️ 아래는 모두 오류 발생
# num_is_iterable = iter(123)
# bool_is_iterable = iter(True)
# mc_is_iterable = iter(MyClass())

pass