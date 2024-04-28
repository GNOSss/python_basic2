#__str__(self) / __repr__(self)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 개발자가 보기 위한 기술적 표현
    def __repr__(self):
        return f'Person({self.name!r}, {self.age})'

    # 사용자가 보기 위한 쉬운 문자열 표현
    def __str__(self):
        return f'{self.name}씨는 {self.age} 살입니다.'


# 💡 디버깅시 어느 쪽이 나오는지 확인
person = Person('김돌준', 30)

person_repr = (repr(person))

person_str = str(person)

# 💡 프린트시 어느 쪽이 나오는지 확인
print(person)

pass