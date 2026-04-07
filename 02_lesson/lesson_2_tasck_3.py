import math

def square(side):
    area = side * side
    return math.ceil(area)

user_input = float(input("Введите сторону квадрата: "))

result = square(user_input)

print(f"Площадь квадрата: {result}")