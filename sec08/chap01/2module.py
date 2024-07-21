from arithmetics import *
# from (불러올 파일) import * <- 모든 메소드

add_4_3 = add(4, 3)
subt_4_3 = subtract(4, 3)
mult_4_3 = multiply(4, 3)
div_4_3 = divide(4, 3)

# _ 로 시작하는 요소는 와일드카드로는 임포트되지 않음
# rest_4_3 = _rest(4, 3)

# arithmetics 에도 add 메소드가 있지만 나중에 작성한(밑에 있는 add) 코드로 적용 됨
# 단, 1줄에 from - import 가 밑에 def add(a,b)보다 밑에 있으면 arithmetics 파일의 add를 사용함
def add(a, b):
    return f"{a} + {b} = {a + b}"

pass

# from (불러올 파일) import (사용할 메소드) as (사용할 메소드를 현 파일에서 호출명 작성)
from arithmetics import add as add_simple
# from (불러올 파일) import_사용할 메소드 ( 기존 메소드명 as 변경할 메소드명)
from arith_w_print import (
    add as add_print,
    multiply as mult_print,
    divide as div_print
)

add_s_3_4 = add_simple(3, 4)
add_p_3_4 = add_print(3, 4)
mult_p_3_4 = mult_print(3, 4)

print(add_s_3_4, add_p_3_4, mult_p_3_4)