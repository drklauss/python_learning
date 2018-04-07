# Написать класс калькулятора, хранящего вещественное число x и понимающего следующие команды:
#
# прибавить к этому числу значение параметра,  вычесть из него, домножить его и разделить,
# а также извлечь из этого числа квадратный корень
# и взять тригонометрическую функцию. Написать еще один класс, кроме перечисленного имеющий одно свойство
# и понимающий команды записать в память, извлечь из памяти, добавить x к содержимому памяти.
import math


class Memory:
    def __init__(self):
        self._mem = 0.00

    @property
    def mem(self):
        return self._mem

    @mem.setter
    def mem(self, value):
        self._mem = value

    @mem.getter
    def mem(self):
        return self._mem

    def mem_plus(self, val):
        self._mem += val
        return self

    def mem_minus(self, val):
        self._mem -= val
        return self


class Calculator(Memory):
    def __init__(self):
        super().__init__()
        self.value = 0.00

    def __str__(self):
        return "{:.2f}".format(self.value)

    def plus(self, val):
        self.value += val
        return self

    def minus(self, val):
        self.value -= val
        return self

    def mul(self, val):
        self.value *= val
        return self

    def div(self, val):
        self.value /= val
        return self

    def square_root(self):
        self.value = pow(self.value, 0.5)
        return self

    def cos(self):
        self.value = math.cos(self.value)
        return self


calc = Calculator()
calc.mem = calc.value
calc.mem_plus(10).mem_minus(5)
print(calc)
print(calc.mem)
