import random

def dice_generator(rolls):
    current_roll = 0
    while current_roll < rolls:
        yield random.randint(1, 6)
        current_roll += 1


for roll in dice_generator(5):
    print(roll)




def fibonacci_generator(count):
    num1, num2 = 0, 1
    for _ in range(count):
        yield num1
        num1, num2 = num2, num1 + num2


numbers = list(fibonacci_generator(10))

pass