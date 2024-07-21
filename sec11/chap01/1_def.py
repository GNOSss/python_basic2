# 프로그래밍에서 일급 객체란 ‘값’(문자,인트,불리언,리스트,튜플 등) 처럼 다뤄질 수 있는 요소를 말합니다.
# 파이썬과 같은 언어에서는 함수도 일급 객체입니다.

# 일급 객체의 4가지 특징
def add(x, y):
    return x + y

def subt(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y


# 💡 다른 변수에 할당
# 변수 자체를 함수 호출로 하지만 매개변수 값을 같이 적용한게 아님
# 다른 변수에 할당하는 건데 , 따로 할당(?) 아니면 나눠서 할당(?) 이라고 적어두겠음
arith_1 = add
add_3_4 = arith_1(3, 4)


# 💡 다른 함수를 반환하는 함수
def get_arith_func(get_add=True):
    return add if get_add else subt
    # return식 해서 :  if get_add 가 True면 add , else면 subt

arith_1 = get_arith_func(True)
arith_2 = get_arith_func(False)


num_1 = arith_1(5, 3)
# arith_1 = get_arith_func 가 True 이고 그 함수가 True 일 경우 add , False 일 경우 subt 함수를 호출 함
num_2 = arith_2(5, 3)




# 💡 다른 함수를 매개변수로 받는 함수
def calculate(arith, x, y):
    # SS풀이  2:  calculate 함수 호출에 받은 인자 값들로 return문에 2번째 함수 호출하여 보냄
    return arith(x, y)

# SS풀이  1:  calculate 함수 호출시 매개변수에 함수 호출과 매개변수 인자 값을 같이 전달
calc_1 = calculate(add, 3, 4)
calc_2 = calculate(mult, 3, 4)




# 💡 함수들을 담은 리스트
arith_list = [add, subt, mult, div]
arith_3_4_results = [arith(3, 4) for arith in arith_list]
# arith_list 를 arith 에 in 한다. 그리고 arith(3,4)로 각각 함수 호출하게 된다.
# 헷갈림 주의  ! arith로 arith_list 순회하고 순회 할때마다 arith(@,@) 식을 만들게 한다는 것

sss1 = arith_list[0](6,8,)
sss2 = arith_list[1](6,8)
sss3 = arith_list[2](6,8)




pass

