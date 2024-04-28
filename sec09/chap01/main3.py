class Person:
    def __init__(self, age):
        self.age = age

    @property
    def korean_age(self):
        return self.age + 1

    @korean_age.setter
    def korean_age(self, kr_age):
        self.age = kr_age - 1


person_1 = Person(17)
per_1_age_a = person_1.age
per_1_kor_age_a = person_1.korean_age

person_1.korean_age = 20
per_1_age_b = person_1.age
per_1_kor_age_b = person_1.korean_age


pass