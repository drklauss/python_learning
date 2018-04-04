import math
import time

HUMAN_VIEW_X = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
}


class Algorithm:
    def __init__(self, start_pt: 'Point', aim_pt: 'Point'):
        self._start_pt = start_pt
        self._aim_pt = aim_pt
        self._solutions = list()
        self._sequence = list()
        self._solution_steps = 0
        self._stat = Statistic()

    def run(self):
        print("Поиск решений: {} -> {}".format(self._start_pt, self._aim_pt))
        self._stat.set_start_time()
        self.stepping(self._start_pt, 0)
        self._stat.set_end_time()
        self.print_result()

    def stepping(self, pt: 'Point', step: int):
        """Ход"""
        self._stat.inc_step()
        if step > 0:
            self._sequence = self._sequence[:step]
        if self._solution_steps > 0:
            if step > self._solution_steps:
                return
        if pt in self._sequence:
            return
        self._sequence.append(pt)
        if pt == self._aim_pt:
            self._solutions.append(self._sequence)
            self._solution_steps = len(self._sequence)
            return
        next_points = pt.get_next_points()
        self._stat.set_pos_points(next_points)

        for next_point in next_points:
            if self.is_distance_decrease(pt, next_point) or self.is_point_near_the_target(next_point):
                self.stepping(next_point, step + 1)

    def is_distance_decrease(self, cur_pt: 'Point', next_pt: 'Point'):
        """Уменьшается ли расстояние до целевой точки"""
        x_diff_cur = math.fabs(cur_pt.x - self._aim_pt.x)
        y_diff_cur = math.fabs(cur_pt.y - self._aim_pt.y)

        x_diff_next = math.fabs(next_pt.x - self._aim_pt.x)
        y_diff_next = math.fabs(next_pt.y - self._aim_pt.y)

        return x_diff_next + y_diff_next <= x_diff_cur + y_diff_cur

    def is_point_near_the_target(self, next_pt: 'Point'):
        """Находится ли текущяая точка возле целевой в пределах одной клетки"""
        return math.fabs(next_pt.x - self._aim_pt.x) <= 1 or math.fabs(next_pt.y - self._aim_pt.y) <= 1

    def print_result(self):
        """Вывод результата на печать"""
        self._stat.print()
        print("Лучшее решение: ")
        for sequence in self._solutions:
            if len(sequence) == self._solution_steps:
                print(sequence)
        if len(self._solutions) > 1:
            print("Еще варианты: ")
            for sequence in self._solutions[len(self._solutions) - 1::-1]:
                if len(sequence) != self._solution_steps:
                    print(sequence)


class Point:
    """Класс работы с координатами точки на шахматной доске"""

    def __init__(self, x: int, y: int):
        if x < 0 or x > 7 or y < 0 or y > 7:
            raise IndexError
        self.x = x
        self.y = y

    def __str__(self):
        for k, v in HUMAN_VIEW_X.items():
            if v == self.x:
                return '{}{}'.format(k, self.y + 1)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def create(name: str) -> 'Point' or None:
        """Создает точку по заданной нотации"""
        tup = tuple(name.lower())
        if len(tup) != 2:
            print('Неверная нотация координат: {}'.format(name))
            return
        try:
            y = int(tup[1])
            x = HUMAN_VIEW_X[tup[0]]
            pt = Point(x, y - 1)
        except (KeyError, ValueError, IndexError):
            print('Неверная нотация координат: {}'.format(name))
            return

        return pt

    def get_next_points(self):
        """Возвращает последующие возможные точки хода"""
        pts = []
        try:
            point1 = Point(self.x + 2, self.y + 1)
            pts.append(point1)
        except IndexError:
            pass
        try:
            point2 = Point(self.x + 2, self.y - 1)
            pts.append(point2)
        except IndexError:
            pass
        try:
            point3 = Point(self.x - 2, self.y + 1)
            pts.append(point3)
        except IndexError:
            pass
        try:
            point4 = Point(self.x - 2, self.y - 1)
            pts.append(point4)
        except IndexError:
            pass
        try:
            point5 = Point(self.x + 1, self.y + 2)
            pts.append(point5)
        except IndexError:
            pass
        try:
            point6 = Point(self.x + 1, self.y - 2)
            pts.append(point6)
        except IndexError:
            pass
        try:
            point7 = Point(self.x - 1, self.y + 2)
            pts.append(point7)
        except IndexError:
            pass
        try:
            point8 = Point(self.x - 1, self.y - 2)
            pts.append(point8)
        except IndexError:
            pass
        return tuple(pts)


class Statistic:
    """Сбор статистики"""

    def __init__(self):
        self.possible_points = list()
        self.steps = 0
        self.startTime = 0
        self.endTime = 0

    def set_start_time(self):
        self.startTime = time.clock()

    def set_end_time(self):
        self.endTime = time.clock()

    def set_pos_points(self, pts: tuple):
        self.possible_points.extend(pts)

    def print(self):
        print("Время выполнения: {0:.3f}с. ".format(self.endTime - self.startTime))
        print("Попыток походить: {} ".format(self.steps))
        print("Потенциальных ходов: {} ".format(len(self.possible_points)))

    def inc_step(self):
        self.steps += 1


print("Программа рассчета количества ходов конем из точки А в В. Пример нотации ввода: b2, c7")
start_point = Point.create(input("Введите точку начала: "))
aim_point = Point.create(input("Введите точку назначения: "))
if isinstance(start_point, Point) and isinstance(aim_point, Point):
    alg = Algorithm(start_point, aim_point)
    alg.run()
