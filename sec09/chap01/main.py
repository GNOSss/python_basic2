class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            print("반지름은 음수가 될 수 없습니다.")

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return 3.14 * self._radius ** 2

# - 속성의 이름과 프로퍼티의 이름은 달라야 함
#     - 같으면 순환오류 발생 (시도해 볼 것)
#     - 관례적으로 속성명 앞에 `_`  을 붙여 구분


circle_1 = Circle(3)

circle_1_rad = circle_1.radius

#29번째 줄의 Circle(3)을 (5)로 변경함
circle_1.radius = 5  # 🔴
#Circle(5)에서 (-2)를 변경하려 했지만 @radius.setter에 if문에 걸려 변경 하지 못함
circle_1.radius = -2

circle_1_diameter = circle_1.diameter
circle_1_area = circle_1.area













