# 클래스가 가질 수 있는 인스턴스 속성을 제한합니다.
# 메모리 사용량을 줄이고 실행속도를 향상시킵니다.

class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Jane', 25)
# p.address = 'Seoul'         # Person 클래스의 p.address = 'Seoul' 추가
                                    #  __slots__ 기능으로 생성자 속성을 더 만들지 못하게 할 수 있음 ⚠️ 불가

# Person 클래스 생성자 속성을 딕셔너리 형태로 생성
# p_dict = p.__dict__         #__dict__도 __slots__사용하면 사용할 수 없음
# print(p_dict)

print(p.__slots__)      #p.__dict__를 사용할 수 없음 p.__slots__으로 사용하면 됨

