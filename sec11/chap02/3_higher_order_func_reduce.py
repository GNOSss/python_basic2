#reduce
#요소들을 주어진 함수대로 '접어 나가' 하나의 값을 반환


from functools import reduce
# 형식 : 변수명 = reduce()
numbers = [1, 2, 3, 4, 5]

# 모든 요소들을 차례로 곱해 나감
# 즉, numbers 의 1,2,3,4,5의 값들을 차례로 매개변수로 넘기는 것
# 1 * 2 후 결과값이 다시 x의 값으로 넘겨져 2 * 3 으로 계산 또 6 * 4 로 계속해서 넘어감
product = reduce(lambda x, y: x * y, numbers)
product1 = reduce(lambda x, y : x*y , numbers , 7)
# 위의 식은 초기값!!!이 있는 예제이다. numbers를 순차적으로 곱하기전에
# 첫 x 를 7으로 매개변수로 넘겨서 식을 계산하는 것




from functools import reduce

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]
# 초기인자가 필요할 시 끝에 넣어줌
total_age = reduce(lambda x, y: x + y['age'], users, 0)
# 초기값 0으로 넣어 줌으로써 매 딕셔너리의 age 값을 int형으로 받아서 계산할 수 있음
# 만약 초기값 0을 넣지 않는다면 x는 첫 딕셔너리 y는 두번째 딕셔너리 넣고 함수에서 에러발생함




from functools import reduce

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_even_count = reduce(
    # 콜백함수
    lambda prev, curr: {
        'odd': prev['odd'] + (curr % 2),
        'even': prev['even'] + (1 - (curr % 2))
#이해를 위해... prev['odd']이게 이해 안됐었는데
#혹시나 해서 기록한다. prev는 초기값으로 딕셔너리를 갖고 있는 거고
# 'odd': prev['odd'] + (curr % 2), 이건 prev라는 딕셔너리의 odd 키의 벨류 값으로 curr % 2 의 반환 값을 넣으라는 것
    },
    # 컬렉션
    arr,
    # 초기값 : 딕셔너리 형태도 가능함
    {'odd': 0, 'even': 0} # 이 딕셔너리는 prev로 넘겨짐
)

print(odd_even_count)




# 고위 sorted : 주어진 기준으로 정렬
data = [-5, -3, 1, 4, -2]
sorted_data = sorted(data, key=lambda x: x ** 2)
# 주의할 사항은 sorted() 함수의 첫번째 인자는 정렬할 데이터를 넣어야 한다는 것

#마찬가지로 sorted() 함수의 첫번째 인자로 정렬할 데이터를 넣고 , key = len 은 기준을 뜻함
words = ["banana", "apple", "cherry", "blueberry"]
sorted_by_length = sorted(words, key=len)

# 주의할 건 sorted()함수에서는 정렬할 데이터와 함수를 지정해야한다
# 함수를 넣을라는 것이아니라 함수명을 넣는 것이지 위2개와 아래1개의 예제는 key라는 함수명을 넣은 것
users = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}]
sorted_by_age = sorted(users, key=lambda x: x['age'])






pass