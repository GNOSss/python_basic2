# currying
# 고난도의 주제입니다.

def add_mult_subt(a, b, c, d):
    return ((a + b) * c) - d

# 또는 아래처럼 람다 함수로
# add_mult_subt = lambda a, b, c, d: ((a + b) * c) - d

result_1 = add_mult_subt(2, 3, 4, 5)


# 만약 4개 매개변수의 값들이 부분적으로만 주어진다면?
# 위에서 배운 lambda는 매개변수가 한 번 실행할때 모두 갖고 있어야한다.
# currying은 lambda 함수 사용할때 필요한 매개변수가 한 번에 다 받을 수 없을때 사용한다
# return lambda b: lambda c: lambda d: (a + b) * c - d 이 식을 해석해보겠다.
# lambda b : 매개변수 c, d, a  가 다 있을때 실행하겠다고 선언
# lambda c : 매개변수 d, a 가 있을때 실행하겠다고 선언

def curry_add_mult_subt(a):
    return lambda b: lambda c: lambda d: (a + b) * c - d

result_2 = curry_add_mult_subt(2)(3)(4)(5)


add_mult_subt_from_2 = curry_add_mult_subt(2) #매개변수 a 받음
result_3 = add_mult_subt_from_2(3)(4)(5)
#나머지 매개변수를 add_mult_subt_form_2 호출과 동시에 ()튜플형태로 집어넣어줌

mult_subt_from_5 = curry_add_mult_subt(2)(3)
result_4 = mult_subt_from_5(4)(5)

subt_from_20 = curry_add_mult_subt(2)(3)(4)
result_5 = subt_from_20(5)