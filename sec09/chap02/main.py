from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass



class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius





# ⚠️ 추상 메서드가 있는 클래스는 생성 불가
# shape = Shape()

rect = Rectangle(3, 4)
r_area, r_perm = rect.area(), rect.perimeter()

circ = Circle(5)
c_area, c_perm = circ.area(), circ.perimeter()


# - 구현되지 못한 추상 클래스가 남아있으면 인스턴스 생성 불가
#     - 자식 클래스에서 구현부 제거해 보고 실행해 볼 것

objs = [1, True, "Hello", rect, circ]

for obj in objs:
    if isinstance(obj, Shape):
        print(obj.area(), obj.perimeter())



