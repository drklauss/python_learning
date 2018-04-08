# Создайте класс с именем Person, содержащий три поля для хранения имени, фамилии и отчества.
# В классе создайте функцию show_data(), выводящую на экран имя, фамилию и отчество.
# Далее от класса Person с помощью наследования создайте два класса: Student, Professor.
# К классу Student добавьте дополнительное поле, содержащее средний бал студента. К классу Professor три поля:
#
# число публикаций профессора,
# должность (тип - перечисление) - преподаватель, старший преподаватель, доцент, профессор,
# возраст. Для каждого производного класса переопределите метод show_data(). В основной программе определите массив.
# Далее в цикле нужно организовать ввод студентов и профессоров вперемешку. Когда ввод будет закончен,
# нужно вывести информацию с помощью метода show_data() обо всех людях.
import enum
import random


class Position(enum.Enum):
    """Должности профессоров"""
    prepod = 'преподователь'
    older_prepod = 'старший преподаватель'
    docent = 'доцент'
    professor = 'профессор'


class Fio:
    """Класс создающий произвольные ФИО"""
    names = ('Сергей',
             'Николай',
             'Валентин',
             'Егор',
             'Александр',
             'Алексей',
             'Олег',
             'Владимир',
             'Михаил',
             'Антон'
             )
    surnames = (
        'Кузнецов',
        'Бокачев',
        'Трубоводов',
        'Алексеев',
        'Жуковский',
        'Никитин',
        'Боярский',
        'Доброедов',
        'Ждунов',
        'Клопов'
    )
    patronymics = (
        'Николаевич',
        'Сергеевич',
        'Никитич',
        'Владимирович',
        'Ибрагимович',
        'Алексеевич',
        'Семенович',
        'Петрович',
        'Викторович',
        'Русланович'
    )

    @staticmethod
    def generate_fio():
        """Генератор ФИО"""
        return random.choice(list(Fio.names)), \
               random.choice(list(Fio.patronymics)), \
               random.choice(list(Fio.surnames))


class Person:
    def __init__(self):
        self.name = None
        self.patronymic = None
        self.surname = None

    def fill_data(self):
        """Заполняет данные личности"""
        self._fill_fio()

    def _fill_fio(self):
        """Заполняет данные ФИО"""
        self.name, self.patronymic, self.surname = Fio.generate_fio()


class Student(Person):
    def __init__(self):
        super().__init__()
        self.avg_mark = 0.00

    def __str__(self):
        return "({}) {} {} {} - {:.2f} б.".format(self.__class__.__name__, self.name, self.patronymic, self.surname,
                                                  self.avg_mark)

    def fill_data(self):
        self._fill_fio()
        self.avg_mark = float(random.randint(3, 4)) + random.random()
        return self


class Professor(Person):
    def __init__(self):
        super().__init__()
        self.position = None
        self.years = None

    def __str__(self):
        return "({}) {} {} {} - {} лет, {}.".format(self.__class__.__name__, self.name, self.patronymic, self.surname,
                                                    self.years, self.position)

    def fill_data(self):
        self._fill_fio()
        pos = random.choice(list(Position.__iter__()))
        self.position = pos.value
        self.years = random.randint(30, 60)
        return self


class PersonsFactory:
    """Фабрика создающая личности"""

    @staticmethod
    def create_person() -> Person:
        """Создает личность Студент или Профессор"""
        person = random.choice((Student(), Professor()))
        person.fill_data()
        return person


for i in range(0, 11):
    per = PersonsFactory.create_person()
    print(per)
