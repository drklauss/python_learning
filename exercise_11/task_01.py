# Создать класс Circle, конструктор которого принимает радиус. Класс должен иметь два метода,
# вычисляющие площадь и длину окружности. Пример вызова класса:
#
# NewCircle = Circle(8)
# print(NewCircle.area())
# print(NewCircle.perimeter())

from math import pi


class Circle:
    def __init__(self, rad: float):
        self.rad = rad

    def area(self) -> float:
        return round(pi * pow(self.rad, 2), 2)

    def perimeter(self) -> float:
        return round(2 * pi * self.rad, 2)


NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
