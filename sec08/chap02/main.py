from myutils import greetings, arithmetics
# from 패키지 즉, 폴더명 import 파일


hello_to_cheolsu = greetings.hello_to("철수")
add_3_4 = arithmetics.add(3, 4)



from myutils.greetings import *
# from 패키지.파일명 import 해당 파일의 모든 메소드
from myutils.arithmetics import add, subtract
# from 패키지.파일명 import 해당 파일의 메소드 명

hello_to_cheolsu = hello_to("철수")
add_3_4 = add(3, 4)
subt_3_4 = subtract(3, 4)



from myutils.subutils import arith_print
# from 겉패키지.안패키지 Import 안패키지의 파일명
from myutils.subutils.cars import Car
# from 겉패키지.안패키지.파일명 Import 해당파일의 메소드


arith_print.divide(10, 3)
print(Car("삼성", "SM3").drive())



from myutils import add
#from myutils의 init 파일 import add 메소드 실해하는데
#myutils의 init파일에는 from .arithmetics import add 이렇게 코드가 되어있어서
#arithmetic의 add 메소드를 바로 사용 가능

from myutils.subutils import Car
# myutls폴더 안에 subutils의 init 파일에 from .cars import Car의 코드가 작성되어 사용 가능함

add_3_4 = add(3, 4)
mycar = Car("메르세데스", "벤츠")


pass