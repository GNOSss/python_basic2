import random
#난수를 생성하는 함수들을 제공

# 💡 시드 설정
# 아래를 활성화하고 값을 바꿔가며 반복 실행해 볼 것
random.seed(10) # << seed()안에 값을 넣으면 같은 값을 출력함. 약간 난수를 저장한다 ?는 개념
## random 모듈로 코드를 작성했을때 같은 값으로 나오게해서 코드 수정, 오류발견 및 수정을 할 수 있게 함

# 임의의 실수 생성
random_float = random.random()

# 범위 내 임의의 정수 생성 (1~10 사이)
random_int = random.randint(1, 10)

# 범위와 스텝을 지정한 임의의 정수 (0~101 사이에 5 간격을 두고)
random_range = random.randrange(0, 101, 5)

# 시퀀스의 임의의 요소 선택 (리스트 형식으로 있어야함)
choice_from_list = random.choice(['apple', 'banana', 'cherry', 'date'])

# 시퀀스를 무작위로 섞기
list_to_shuffle = [1, 2, 3, 4, 5]
random.shuffle(list_to_shuffle)

# 시퀀스에서 지정된 개수의 요소를 무작위로 선택 (리스트형식의 시퀀스 , 갯수)
sample_from_list = random.sample([10, 20, 30, 40, 50], 3)

pass