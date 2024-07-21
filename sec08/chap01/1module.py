#import할때 파일명(greetings)를 적어서 실행한다.
import greetings
import page_elements

# greetings 사용
# 변수 사용
greetings_version = greetings.version

# 메소드 사용
hello_to_cheolsu = greetings.hello_to("철수")
bye_to_yeonghee = greetings.bye_to("영희")

# page_elements 사용
a_button = page_elements.Button("a")
a_button.click()

from arithmetics import add, divide, _rest
## 실행할 파일의 일부 기능(메소드)만 사용할때 위처럼 작성 가능
## from(파일명) import (파일에서 사용할 기능들)

add_3_4 = add(3, 4)
divide_12_2 = divide(12, 2)
rest_10_3 = _rest(10, 3) # 이처럼 위에 지정하면 임포트됨



from arithmetics import add, divide

from car import Car
from electric_car import ElectricCar

my_car = Car("기아", "K5")
my_car_dsc = my_car.description()
my_car_drive = my_car.drive()

my_electric_car = ElectricCar("테슬라", "모델 3")
my_el_car_desc = my_electric_car.description()
my_el_car_drive = my_electric_car.drive()
my_el_car_charge = my_electric_car.charge()


#__name__내장변수
#현재 모듈의 이름들을 나타낸다. 현재 파일에서 실행되면 __main__으로 출력됨
#다른파일들은 파일명들이 나오게 된다.
#import했던 파일들에 각각 (특정명, __name__)하게되면 import했던 파일들이 모두 프린트됨
print(1, __name__)

# def function():
#     print("함수가 실행됩니다.")
#
# if __name__ == "__main__":
#     function()




pass