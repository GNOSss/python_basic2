from car import Car


class ElectricCar(Car):
    def __init__(self, make, model):
        super().__init__(make, model)

    def charge(self):
        return f"{self.model} 충전중"



print(4, __name__)