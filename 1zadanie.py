import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

if __name__ == "__main__":
    radius1 = float(input("Введите радиус первой окружности: "))
    circle1 = Circle(radius1)

    radius2 = float(input("Введите радиус второй окружности: "))
    circle2 = Circle(radius2)

    if circle1 == circle2:
        print("Радиусы окружностей равны")
    elif circle1 > circle2:
        print("Первая окружность больше второй по радиусу")
    elif circle1 < circle2:
        print("Первая окружность меньше второй по радиусу")

    change = float(input("Введите число для изменения радиуса первой окружности: "))
    circle1 += change
    print("Новый радиус первой окружности после увеличения:", circle1.radius)

    change = float(input("Введите число для изменения радиуса второй окружности: "))
    circle2 -= change
    print("Новый радиус второй окружности после уменьшения:", circle2.radius)
