# iterator
# 이터러블 안에 든 아이템을 하나씩 돌며(순회) 반환하는 객체입니다.
# 다음 아이템을 반환하는 __next__ 매직 메소드를 갖습니다.
# next() : 이터레이터에서 현 차례의 값 반환
    # - 상태가 기록됨

iterable_list = [1, 2, 3]
iterable_tuple = (4, 5, 6)
iterable_string = "abc"

# 이터레이터(iterator)를 만드는 방법
# 1) 위 자료들을 iter()로 묶어줌
iterator_list = iter(iterable_list)
iterator_tuple = iter(iterable_tuple)
iterator_string = iter(iterable_string)
# 2) iter()로 묶은걸 __next__ 메소드로 실행 , next() 이걸로 묶어줌
# 2-1) 하단은 첫번째 이터레이터
lst_val_0 = next(iterator_list)
tpl_val_0 = next(iterator_tuple)
str_val_0 = next(iterator_string)
# 2-2) 하단은 두번째 이터레이터
lst_val_1 = next(iterator_list)
tpl_val_1 = next(iterator_tuple)
str_val_1 = next(iterator_string)

###### iter()를 활용할때 iter()안에있는 요소 값을 100%그대로 사용하고 싶다면
###### 재정의를 계속 해줘야한다. 

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)  # 리스트에서 이터레이터 생성

# 반복문과 next() 함수로 이터레이터의 모든 요소 순회
while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        # 모든 요소를 순회하면 StopIteration 예외 발생
        break


# 리스트로 바꾸기 1 (리스트 생성자)
my_iter = iter(my_list) # 💡 이터레이터는 1회용이므로 재정의 (빼고 해 볼 것)
list_from_iter_1 = list(my_iter)

# 리스트로 바꾸기 2 (컴프리헨션)
my_iter = iter(my_list)
list_from_iter_2 = [num for num in my_iter]


pass