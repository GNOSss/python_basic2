# 딕셔너리 생성 및 초기화
my_dict = {"name": "Alice", "age": 25, "city": "New York", "job": "designer"}

# 요소 추가 및 수정
my_dict["email"] = "alice@example.com"  # 새로운 요소 추가
my_dict["age"] = 26  # 기존 요소 수정


# 키 유무 확인
key_exists_1 = "name" in my_dict
key_exists_2 = "bloodtype" in my_dict

# 요소 접근
age1 = my_dict["age"]
age2 = my_dict.get("age")

# 💡 없는 요소에 접근시
# bloodtype = my_dict["bloodtype"] # 이 방식으로 하면 오류 발생
bloodtype = my_dict.get("bloodtype")

# 요소 삭제
deleted_value = my_dict.pop("city")  # 'city' 키를 가진 요소를 삭제하며 반환
del my_dict["job"] # 삭제만 하고 그 값을 반환하지는 않음

# 키, 값, 아이템
# 💡 dict_keys, dict_values, dict_items 자료형 반환
# 이후 배울 이터러블의 일종
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

for key in keys:
    print(key)

# 리스트로 변환
keys_list = list(keys)
values_list = list(values)
items_list = list(items)

# 💡 items()로 반환된 각 쌍의 자료형 확인
item_type = str(type(items_list[0]))

# 딕셔너리 복사
# 💡 이후 변화 확인
my_dict_copy = my_dict.copy()

# 다른 딕셔너리로부터 아이템들을 가져옴
# 💡 딕셔너리의 키로 모든 불변 객체 사용 가능 확인
another_dict = {3.14: "PI", ("흥부", "놀부"): "brothers"}
my_dict.update(another_dict)

# 딕셔너리 비우기
my_dict.clear()

pass