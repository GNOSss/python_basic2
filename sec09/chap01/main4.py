class Employee:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name[0] + '모씨'

    @property
    def age(self):
        return str(self._age - (self._age % 10)) + '대'

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age

    def get_older(self, years):
        self._age += years


emp_1 = Employee('김복동', 22)

emp_1_name = emp_1.name
emp_1_age_a = emp_1.age

emp_1.get_older(12)
emp_1_age_b = emp_1.age

emp_1.age = 0
emp_1_age_c = emp_1.age

pass