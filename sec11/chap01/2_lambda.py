# 람다함수
# 람다 함수는 일급 객체로서 일회성으로 사용되기 위한 익명 함수,
# 즉 따로 이름을 부여하여 어딘가 저장하지 않은 함수입니다.
# 파이썬의 람다 함수는 한 줄로만 지정할 수 있습니다.
    # 복잡한 로직은 def 정의 함수로
    # 이후에 배울 고위 내장함수들에 사용됩니다.

# 형식 :  함수명 =  lambda 매개변수값 : retrun형식문
add = lambda x, y: x + y
result_add = add(5, 3)
# 비슷한 방식으로 아래 처럼 쓸 수 있음
result_add2 = (lambda x, y : x + y)(5,3)

# 아래 식은 x가 lambda 함수의 매개변수고 그 값이 x 보다 크면 "Positive"로 return 하는 식
check_positive = lambda x:  "Positive" if x > 0 else "Non-positive"
positive_check_result = check_positive(-5)



# num_ 변수에 arith_(5,3) 각각 갖고 있다. 그 arith_ 에는 get_arith_func()을 갖고 있고
# 하나는 True를 , 하나는 False를 갖고 있어 def get_arith_func() 에 매개변수에 맞게 lambda식으로 반환함
# 매개변수에 따라 lambda식이 반환되어 num_1 과 num_2에 결과값이 반환하게 됨
def get_arith_func(get_add=True):
    return (lambda x, y: x + y) if get_add else (lambda x, y: x - y)


arith_1 = get_arith_func(True)
arith_2 = get_arith_func(False)


num_1 = arith_1(5, 3)
num_2 = arith_2(5, 3)




# def calculate에 매개변수를 3개를 넘겨줌.
# x,y는 int형 자료를 넘기지만 arith에는 함수형 자료를 넘겨준다.
# 즉 함수와 실제 활요되는 매개변수를 넘겨줌으로써 def calculate에서 실행하고 반환하게 끔 한다.
def calculate(arith, x, y):
    return arith(x, y)

calc_1 = calculate(lambda x, y: x + y, 3, 4)
calc_2 = calculate(lambda x, y: x * y, 3, 4)




# 리스트는 str형, float형, int형 외에도 def함수(여기선 Lambda)를 넣을 수 있다.
# arith_3_4_result 에는 arith_list를 arith가 순회하면서 arith(3,4)에 하나씩 한번씩
# 실행하문 코드문이다.
arith_list = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x / y
]

arith_3_4_results = [arith(3, 4) for arith in arith_list]





# 아래 식은 조금 귀찮게 꼬아 놓았음.
# 1) add, sub, mul, div 각각 lambda 식으로 함수를 선언했음
# 2) def comb_3_ariths 로 코드 식을 만들어 놓음 (3개의 함수 매개변수를 받음)(
# 2-1) return문의 경우 arith_1 x,y의 결과 값이 arith_2 의 x 가 된다. 그렇게 arith_2 x,y의 결과 값이 arith_3 의 x값으로 위치함
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

def comb_3_ariths(arith_1, arith_2, arith_3):
    return lambda x, y: arith_3(arith_2(arith_1(x, y), y), y)

# comb_3_ariths 작성 후 위위에서 작성한 lambda 식 선언한 변수명을 매개변수로 활용
add_mul_sub = comb_3_ariths(add, mul, sub)
mul_add_div = comb_3_ariths(mul, add, div)
div_add_mul = comb_3_ariths(div, add, mul)

result_1 = add_mul_sub(10, 4)
result_2 = mul_add_div(10, 4)
result_3 = div_add_mul(10, 4)





pass