class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def description(self):
        return f"{self.make} {self.model}"

    def drive(self):
        return f"{self.model} 운전중"


class ElectricCar(Car):
    def __init__(self, make, model):
        super().__init__(make, model)

    def charge(self):
        return f"{self.model} 충전중"