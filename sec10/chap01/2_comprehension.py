# 리스트, 사전, 집합과 같은 컬렉션 데이터 타입을
# 간결하고 효율적으로 생성할 수 있는 방법입니다.
# 이터러블(iterable)에는 컴프리헨션(comprehension)이 필수로 들어가야함

# 기본
basic_list = [x for x in range(10)]
# x에 range(10)을 통해 0~9까지 하나씩 받아서 리스트[]열에 담는다

basic_list_2 = [x + 2 for x in range(10)]
# x 를 range(10)를 통해 0~9까지 하나씩 리스트[]에 넣는데 +2를 한 값들을 넣는 것
basic_list_2 = [x * 3 for x in range(10)]
# x 를 range(10)를 통해 0~9까지 하나씩 리스트[]에 넣는데 *3을 한 값들을 넣는 것


# 조건 : if문 사용
even_numbers = [x for x in range(10) if x % 2 == 0]
# x 컴프리헨션에 0~9까지 생성하고 for문을 돌리는데 x 컴프리헨션가 % 2 한 결과가 == 0 이면 담는다.

# 다중 조건
selected_numbers = [x for x in range(20) if x % 2 == 0 if x % 3 != 0]
# x 컴프리헨션에 0~20까지 생성하고 for문을 돌리는데 x 컴프리헨션가 % 2 결과가 == 0 이고 % 3 != 0 이면 담는다.


# 딕셔너리로 변환
words = ["apple", "banana", "cherry"]
word_lengths = {x: len(x) for x in words}
# words 리스트를 x 컴프리헨션에 담아서 for을 돌린다.
# x 는 words 리스트 값들이 한개씩 담길 것이고 : len(x)는 담겨있던 words의 길이를 벨류로 형성된다.
# 딕셔너리 생성시 {} 대괄호를 사용해야함

odd_n_even = {num: ("홀수" if num % 2 else "짝수") for num in range(5)}
# range(0~4)를 생성 후 num 컴프리헨션에 담아 딕셔너리를 생성하는데
# if num % 2 가 True(1)면 홀수 False(0)면 짝수로 반환한 값을 벨류로 형성하게끔 한다.
# if 좌측에는 True의 반환값 ,  else 우측에는 False의 반환값


# 연산
small_squares = {x**2 for x in range(10) if x**2 < 50}
#range(10)으로 0~9까지 x를 x**2하면 담을 것이지만 if x**2 < 50 식에 참인 경우만 넣는다
# 대괄호 {} 중괄호 [] 상관없음



# 중첩
matrix = [[row + col for col in range(3)] for row in range(3)]
# matrix = []
# for row in range(3):
#     matrixxx = []
#     for col in range(3):
#         matrixxx.append(row+col)
#     matrix.append(matrixxx)
# 해당 식 줄임 표현


# 중첩 해체
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [num for sublist in nested_list for num in sublist]
# 해당 식 유사 표현 [(담길 변수명) for (순회명) in (리스트,인스턴스) for (담길 변수명) in (첫 순회해서 담긴 값)]
# result = []
# for sublist in nested_list:
#    for num in sublist:
#         result.append(num)
# print(result)


# 중첩 사전
nested_dict = {row: {col: row * col for col in range(3)} for row in range(5)}
# 모르겠다





