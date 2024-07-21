#주어진 조건에 따라 특정 작업을 반복적으로 실행합니다.

# 기본 사용: 0부터 4까지의 숫자 반복
for i in range(5):
    # i는 0부터 4까지 순차적으로 증가
    print(f"기본 사용: {i}")

# 값 사용 없이 단순반복시 : _ 사용 (컨벤션)
for _ in range(5):
    print("그냥 반복 프린트")

# 시작과 끝 지정: 2부터 5까지의 숫자 반복
for i in range(2, 6):
    # i는 1부터 5까지 순차적으로 증가
    print(f"시작과 끝 지정: {i}")

# 증가폭 지정: 0부터 10까지 2씩 증가하며 숫자 반복
for i in range(0, 11, 2):
    # i는 0부터 시작하여 2씩 증가하며 10까지 이동
    print(f"증가폭 지정: {i}")

# 감소하는 범위: 5부터 1까지 역순으로 숫자 반복
for i in range(5, 0, -1):
    # i는 5부터 시작하여 1씩 감소하며 1까지 이동
    print(f"감소하는 범위: {i}")

# 중첩 사용
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    if i < 9:
        print("- - - - -")

my_range = range(5)  #my_range = range(0,5)
pass

# 문자열의 문자 순회
my_str = "안녕하세요!"
# for문으로 my_str 문자를 하나씩 빼서 char에 담아서 출력
for char in my_str:
    print(char)

# 리스트 요소 순회
fruits = ["사과", "바나나", "체리"]
#  for문으로 fruits 리스트값을 [0]부터 [2]까지 하나씩 출력함
for fruit in fruits:
    print(f"과일: {fruit}")

# 딕셔너리 키 순회
person = {"이름": "홍길동", "나이": 30, "키": 179.9}
# for문으로 person의 dir의 key를 접근하여 출력
# {person[key]}는 person dir에다가 각key값을 넣어서 value값을 출력
for key in person:
    print(f"{key}: {person[key]}")


# 튜플과 셋에서도 사용 가능
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)
# 셋은 순서가 없으므로 순서 보장 안 됨
# - 순서대로 되는 것처럼 보여도 그것에 의존하여 작성하지 말 것
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)



my_list = ["ABC", (1, 2, 3), {4, 5}, {6: 7, 8: 9}]
#my_list의 요소를 하나 꺼내어 sublist에 담음
for sublist in my_list:
    #sublist에 담긴걸 item으로 쪼개서 담음
    for item in sublist:
        print(item)



# 인덱스와 함께 순회
fruits = ["사과", "바나나", "체리"]
#enumerate가 fruits리스트의 값을 @번째 꺼낼때마다 index에 @번째인지 넘겨줌
for index, fruit in enumerate(fruits):
    print(f"인덱스 {index+1} 번째 : {fruit}")

fruits = ["사과", "바나나", "체리"]
#그러나 for 뒤에 인스턴스(?)를 1개만 설정하면 튜플형태로 반환함
for fruit in enumerate(fruits):
    print(f"{fruit}")

# break : 반복을 종료
# range는 9번을 지시하지만 if문에 == 5번째로 break를 걸면 반복문 종료됨
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue : 다음 턴으로 건너뜀
for i in range(1, 10):
    # i 가 짝수이면 i % 2 는  0이다. 0은 불리언에서 False이지만 not i % 2 이므로 반대로 True로 전환
    if not i % 2:
        continue
    print(i)


