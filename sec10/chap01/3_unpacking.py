#언패킹(unpacking)은 이터러블 안의 요소들을 여러 변수에 할당하는 과정입니다.

# 기본 언패킹
numbers = [1, 2, 3]
a, b, c = numbers

coordinates = (10, 20)
x, y = coordinates

name = "Tom"
f, m, l = name


# 여러 값을 반환하는 함수에서의 언패킹
def get_coordinates():
    return (55.7558, 37.6173)

latitude, longitude = get_coordinates()



# 스타 표현식으로 언패킹
# copy() 처럼 요소를 모두 복사
# 다른 점 : copy는 리스트에만 있음

nums_1 = [1, 2, 3, 4, 5]
nums_2 = [*nums_1]
# nums_3 = nums_1.copy() #.copy() 와 [*nums_1]하고 동일
# nums_1 하고 nums_2는 다르다는 것

# nums_1[0] = 10



# 나머지 뒷부분 언패킹
numbers = [1, 2, 3, 4, 5, 6]
# first, *rest = numbers
first, second, *rest = numbers
# first = 1 , second = 2, rest = 3,4,5,6 으로 패킹됨



# 나머지 가운데 부분 언패킹
tup = (1, 2, 3, 4, 5)
first, *middle, last = tup
#first = 1 , last = 5 , middle = 2,3,4 로 패킹됨




# 여러 이터러블 합치기
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [list1, list2]
combined_list = [*list1, *list2]
# [list1,list2]와 [*list1,*list2] 동일하게 [1,2,3,4,5,6]으로 나옴





# 사전 언패킹 - ** 사용
person_info = {"name": "Alice", "age": 30, "city": "New York"}
new_person = {"gender": "female", **person_info}
# new_person 자료 값에 person_info가 딕셔너리 형태로 붙음


# 이중 별표(**)를 사용하여 여러 사전 합치기
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined_dict = {**dict1, **dict2}
# combined_dict에 dict1 , dict2가 붙어서 나옴




pass