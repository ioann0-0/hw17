import math

class Complex:
    def __init__(self, pervoe, vtoroe):
        self.pervoe = pervoe
        self.vtoroe = vtoroe

    def __add__(self, other):
        return Complex(self.pervoe + other.pervoe, self.vtoroe + other.vtoroe)

    def __sub__(self, other):
        return Complex(self.pervoe - other.pervoe, self.vtoroe - other.vtoroe)

    def __mul__(self, other):
        pervoe_part = self.pervoe * other.pervoe - self.vtoroe * other.vtoroe
        vtoroe_part = self.pervoe * other.vtoroe + self.vtoroe * other.pervoe
        return Complex(pervoe_part, vtoroe_part)

    def __truediv__(self, other):
        denominator = other.pervoe**2 + other.vtoroe**2
        pervoe_part = (self.pervoe * other.pervoe + self.vtoroe * other.vtoroe) / denominator
        vtoroe_part = (self.vtoroe * other.pervoe - self.pervoe * other.vtoroe) / denominator
        return Complex(pervoe_part, vtoroe_part)

    def __str__(self):
        return f"({self.pervoe} + {self.vtoroe}i)"

if __name__ == "__main__":
    pervoe1 = float(input("Введите действительную часть первого комплексного числа: "))
    vtoroe1 = float(input("Введите мнимую часть первого комплексного числа: "))
    complex1 = Complex(pervoe1, vtoroe1)

    pervoe2 = float(input("Введите действительную часть второго комплексного числа: "))
    vtoroe2 = float(input("Введите мнимую часть второго комплексного числа: "))
    complex2 = Complex(pervoe2, vtoroe2)

    result_slojenie = complex1 + complex2
    result_vichitanie = complex1 - complex2
    result_umnojenie = complex1 * complex2
    result_delenie = complex1 / complex2

    print(f"Сумма: {result_slojenie}")
    print(f"Разность: {result_vichitanie}")
    print(f"Произведение: {result_umnojenie}")
    print(f"Частное: {result_delenie}")
