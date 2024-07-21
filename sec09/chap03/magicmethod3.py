class Army:
    def __init__(self, generals, infantry, calvary):
        self.generals = generals
        self.infantry = infantry
        self.calvary = calvary

    def __add__(self, other):
        return Army(
            [self.generals[0], other.generals[0]],
            self.infantry + other.infantry,
            self.calvary + other.calvary
        )

# 기병은 보병 3명 무력으로 가정
#  비교 연산
    def __eq__(self, other):
        return (self.infantry + (self.calvary * 3)) == (other.infantry + (other.calvary * 3))
# 좌측 < 우측
    def __lt__(self, other):
        return (self.infantry + (self.calvary * 3)) < (other.infantry + (other.calvary * 3))
# 좌측 > 우측
    def __gt__(self, other):  #eq(==)도 아니고 lt(<)도 아닌 것 , 즉 (>)
        return not (self == other or self < other)


army_1 = Army(["관우", "장비"], 500, 300)
army_2 = Army(["하후돈", "장료"], 800, 400)
army_3 = Army(["태사자", "황개"], 700, 200)

# amry_4라는 새로운 생성자가 생기게 되는 것
# army_1 + army_2 코드 식 자체가 __add__ 메소드를 호출하게되는 것
# __add__메소드에 self는 army_1 , other에는 army_2가 전달받에 된다.
army_4 = army_1 + army_2
# 연속 계산도 가능
# army_1 과 army_2 를 1차적으로 계산 후 amry_3를 계산하게 됨
# generals의 결과 값은 관우 와 태사자로 결정됨
army_5 = army_1 + army_2 + army_3

# __eq__는 == , __lt__는 < , __gt__는 > 로 함수 호출 됨
army_1_lt_army_3 = army_1 < army_3 #False
army_1_gt_army_3 = army_1 > army_3 #True



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Point 객체 생성
p = Point(3, -5)

# 단항 음수 연산 적용
neg_p = -p


pass

pass