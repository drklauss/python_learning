# Создать класс Rectangle, конструктор которого принимает длину и ширину.
# Класс должен иметь два метода, вычисляющие площадь и периметр прямоугольника.


class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return round(self.length * self.width)

    def perimeter(self) -> float:
        return round(2 * (self.length + self.width))


NewRect = Rectangle(2, 3)
print(NewRect.area())
print(NewRect.perimeter())
