print("myutils/subutils가 임포트되었습니다.")

from .cars import Car
# from 현재경로(.)모듈명 import 메소드


from .arith_print import *

def all_arith_print(x, y):
    add(x, y)
    subtract(x, y)
    multiply(x, y)
    divide(x, y)