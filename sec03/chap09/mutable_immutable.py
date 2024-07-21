# 정수
int_1 = 1
# int_1은 1을 담은 객체가 저장된 곳을 가리킴
int_1_id = id(int_1) # 🔴

#id 는  C언어의 포인터 &와같은 기능하는듯

int_2 = int_1
# int_2는 int_1과 같은 곳을 가리킴
int_2_id = id(int_1)
int_1_is_2_a = int_1 is int_2

int_1 = 2
# 수정하려 하면 저장된 곳의 값이 바뀌는 것이 아니라
# 새로운 값이 담긴 객체가 만들어지고 그곳을 가리킴
int_1_new_id = id(int_1)
int_1_is_2_b = int_1 is int_2
# 2줄의 int_1 = 1 였지만 13줄에서 int_1 = 2로 변경하였기에 주소값이 다름

# 실수
float_1 = 1.0
float_2 = float_1
float_2 = 2.0

# 불리언
bool_1 = True
bool_2 = bool_1
bool_1 = False

# 문자열
str_1 = "Hello"
str_2 = str_1
str_2 = "안녕"

# 튜플
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = tuple_1
tuple_1 = (6, 7, 8, 9)

# 리스트
list_1 = [1, 2, 3, 4, 5]
list_1_id_a = id(list_1) # 🔴

# 다른 변수에 값을 할당
# 집의 주소를 복사해서 주는 것과 같음
# 즉 같은 집의 주소를 갖고 있는 것
list_2 = list_1
list_2_id = id(list_2)

# 리스트 안의 요소 변경
# 집 안의 가구를 바꾸는 것과 같음
list_1[0] = 10
list_1_id_b = id(list_1)

# 다른 값을 할당
# 본인만 새 집으로 이사가는 것과 같음
list_1 = [6, 7, 8]
list_1_id_c = id(list_1)

# 셋
set_1 = {1, 2, 3}
set_2 = set_1
set_1.add(4)

# 딕셔너리
dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = dict_1
del dict_1["a"]

pass