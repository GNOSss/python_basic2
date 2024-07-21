# filter
# 주어진 함수에서 True 를 반환하는 요소들만 걸러 냄
# 역시 컴프리헨션으로 대체 가능


numbers = [1, 2, 3, 4, 5, 6, 7]

odd_filtered = filter(lambda x: x % 2, numbers)
type_odd_filtered = type(odd_filtered).__name__

# 역시 이터레이터임 확인
# filter도 지연 연산을 함 그래서 next가 필요함
first, second = next(odd_filtered), next(odd_filtered)

odds = list(filter(lambda x: x % 2, numbers))
# numbers 각 값을 x로 받아서 x % 2를 하고 그 값이 1이면 즉 True이고 그걸 list로 반환
evens = list(filter(lambda x: not x % 2, numbers))
# numbers 각 값을 x로 받아서 not x % 2를 하고 그 값이 0의 not 이면 즉 True이고 그걸 list로 반환

# 위 lambda식으로 컴프리헨션으로 코드식 작성
odds_2 = [x for x in numbers if x % 2]
evens_2 = [x for x in numbers if not x % 2]




words = ["apple", "banana", "apricot", "cherry", "avocado"]
a_words = list(filter(lambda word: word.startswith('a'), words)) #.startswith(첫 글자가 ('a')라면 True를 반환
# startswith에서 True와 False 나뉜 것중 filter로 True만 골라네고 list로 묶는다

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]
age_above_30 = list(filter(lambda user: user["age"] > 30, users))
# lambda 조건식이 user:user["age:] > 30 인데 , 자칫 name 은 어떻게 들어가는 거지 ? 라고 생각할 수 있지만
# users 는 딕셔너리 구조로 users[1] 은 {"name": "Bob", "age": 30} 이것임
# 그래서 ["age"]라는 특정 키 값을 기준 값으로 정해서 출력하는 것임



pass