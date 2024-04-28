#import * 으로 지정 될 것들을 설정 할 때
__all__ = ["add", "multiply", "ElectricCar"]


def add(x, y):
    print(f"{x} + {y}")
    return x + y


def subtract(x, y):
    print(f"{x} - {y}")
    return x - y


def multiply(x, y):
    print(f"{x} * {y}")
    return x * y


def divide(x, y):
    print(f"{x} / {y}")
    return x / y


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