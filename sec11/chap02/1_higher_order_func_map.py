# 고위내장함수
# 다른 함수를 매개변수로 받는 함수를 고위 함수라고 합니다. (즉, A함수를 인자로 받아 사용하는 함수)
# 반대로, 다른 함수에 매개변수로 들어가는 함수를 콜백 함수라 부르기도 하죠 (즉, B함수에 인자로 사용되는 A함수)

# map
# 컬렉션(튜플,리스트,딕셔너리,셋)의 요소 하나하나를 주어진 함수를 사용하여 변환
# 파이썬에서는 컴프리헨션으로 쉽게 대체

def square(x):
    print(f"{x} * {x}") # 언제 실행되는지 확인
    return x * x
## 강의에서 lambda를 사용할 수 없는 이유가 print 기능때문에 사용 할 수 없다고 함


numbers_list = [1, 2, 3, 4, 5]
#map() 고위 내장 함수 , square는 numbers_list 컬렉션을 활용하는 콜백함수 역할을 한다.
#map()함수 형식 : map(콜백함수명, 컬렉션명)
#단 print 함수는 실행되지 않음 !!!! 주의 !!!
squared_numbers = map(square, numbers_list)
# 만약 square 함수의 print 를 하고 싶으면 하단 처럼 list()로 다시 묶어줘야함
squared_numbers = list(map(square, numbers_list))
print(squared_numbers)

# map 클래스의 객체 - 지연 계산
squared_numbers_type = type(squared_numbers).__name__
# type(squared_numbers).__name__ 해도 map이라는 타입으로 출력됨

# 이터레이터의 일종임 확인
# 💡 실행창 확인!
# squared_number_0 = next(squared_numbers) #출력은 되고 1 * 1로  나옴
# squared_number_1 = next(squared_numbers) #출력은 되고 2 * 2로 나옴
# next는 이터레이터의 일종이고 1단계 , 1단계 진행되게끔 하는 코드문
# - `map` 클래스의 객체 - 결과값이 ‘사용되는 시점에’ 연산
#     - 지연된 계산 *lazy evaluation*

# 아래를 활성화
squared_numbers_list = list(squared_numbers)


# 컴프리헨션으로 대체
squared_numbers_list_2 = [x * x for x in numbers_list]

doubled_list = list(map(lambda x: x * 2, numbers_list))



words = ["Python", "Java", "JavaScript", "C++", "Ruby"]

#words 를 lambda item: 매개변수로 보내고 item.upper()하여 리턴하라
#map(콜백함수명 lambda item: item.upper(), 컬렉션 words))
upper_case_words_1 = list(map(lambda item: item.upper(), words))

# 아래와 같이 간편한 사용도 가능
upper_case_words_2 = list(map(str.upper, words)) #str : 문자열을 뜻함 , .upper 문자열을 대문자로 바꿔주는 함수
lower_case_words = list(map(str.lower, words))
# str.upper("hello")를 해주면 HELLO로 출력된다 .  str.upper의 매개변수로 hello가 들어갔기 때문
str_upper_exp = str.upper("hello")

pass


pass