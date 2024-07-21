class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Point 객체 생성 , main.py의 __repr__ 메소드 참고
p = Point(3, -5)

# 단항 음수 연산 적용 , (-)를로 __neg__ 메소드 사용 가능
neg_p = -p


pass