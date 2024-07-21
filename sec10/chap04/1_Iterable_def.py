my_list = [3, 1, 4, 1, 5, 9, 2]

# len : 길이 반환
my_list_len = len(my_list)

# sorted : 정렬된 [리스트] 반환 (원본은 유지 -  .sort() 함수는 원본을 변경하는 것 sorted와 차이 있음)
my_list_sorted = sorted(my_list)

# reversed : 순서를 뒤집은 [이터레이터] 반환 (원본은 유지 .reverse() 함수는 원본을 변경하는 것 reversed와 차이 있음)
my_list_reversed_itr = reversed(my_list_sorted)
rev_itr_type = type(my_list_reversed_itr).__name__  #type이  iterator 임.list_reverseiterator반환함
print(rev_itr_type)
# 리스트로 변환하여 사용
my_list_reversed = list(my_list_reversed_itr)



# max, min, sum : 최대값과 최소값, 총합
num_list = [1, 2, 3, 4]

num_max = max(num_list)
num_min = min(num_list)

num_sum = sum(num_list)



import random

def dice_generator(rolls):
    current_roll = 0
    while current_roll < rolls:
        yield random.randint(1, 6)
        current_roll += 1


roll_5_sum_1 = sum(dice_generator(5))
roll_5_sum_2 = sum(dice_generator(5))
roll_5_sum_3 = sum(dice_generator(5))




# zip : 여러 이터러블을 묶음
nums = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c']

zipped = zip(nums, letters)
zipped_type = type(zipped).__name__  #type = 'zip'으로 나옴

# 튜플들이 든 리스트
# 개수가 적은 쪽에 맞춰짐
zipped_list = list(zipped)  #zipped_list = [(1,'a'),(2,'b'),(3,'c')]로 나옴

strs = ("Hello", "World", "안녕하세요")

zipped_3 = zip(nums, letters, strs)
zipped_3_list = list(zipped_3)



# enumerate : 각 요소를 인덱스와 함께 튜플로 묶음
fruits = ['apple', 'banana', 'cherry', "orange", "mango"]

enum_fruits = enumerate(fruits)
enum_fruits_type = type(enum_fruits).__name__ #type = enumerate 로 나옴

enum_fruits_list = list(enum_fruits)
enum_fruits_list_types = [type(item) for item in enum_fruits_list]
print(enum_fruits_list)
print(enum_fruits_list[0])
print(enum_fruits_list[0][0])
print(f"{enum_fruits_list[0][0]+1}번째 과일은 {enum_fruits_list[0][1]}입니다.")

print(
    "\n".join([f"{idx + 1} : {fruit}" for idx, fruit in enum_fruits_list])
)
# 리스트로 안묶어도 출력은 됨 / 위 처럼 리스트 사용시 재사용에 용이 , 아래처럼 튜플만 쓰면 메모리 효율성이 좋아짐, 재사용불가
print(
    "\n".join(f"{idx + 1} : {fruit}" for idx, fruit in enum_fruits_list)
)



# all : 모든 요소가 True인가 여부
all_1 = all([True, True, True])
all_2 = all([True, True, False])

numbers = [1, 2, 3, 4, 5] # 음수를 넣어볼 것
are_all_positive = all(x > 0 for x in numbers)
# numbers 요소를 x 에 매번 담고 x > 0 에 참인지 거짓인지 for문을 통해 확인한다.


# any : 하나라도 주어진 함수에 True 반환 여부
any_1 = any([False, False, False])
any_2 = any([False, False, True])

numbers = [1, 2, 3, 5]
is_zero_present = any(x == 0 for x in numbers)



# 문자열 리스트에서 모든 문자열이 특정 길이 이상인지 확인하는 예제
words = ['apple', 'banana', 'cherry']
are_all_longer_than_five = all(len(word) > 5 for word in words)

# if any(len(word) > 5 for word in words) :
#     print(f"{words}의 텍스트는 트루입니다.")
# else:
#     print(f"{words}의 텍스트는 펄스입니다.")






pass