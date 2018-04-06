# Разработать три класса, которые следует связать между собой, используя наследование:
#
# класс Product, который имеет три элемент-данных — имя, цена и вес товара (базовый класс для всех классов);
# класс Buy, содержащий данные о количестве покупаемого товара в штуках, о цене за весь купленный товар и о весе товара
# (производный класс для класса Product и базовый класс для класса Check);
# класс Check, не содержащий никаких элемент-данных. Данный класс должен выводить на экран информацию о товаре и о
# покупке ( производный класс для класса Buy);
#
# Программа должна содержать массив, заполненный объектами производных классов. В программе должно демонстрироваться
# использование всех разработанных элементов классов.


class Format:
    liter = 'л.'
    kg = 'кг.'
    piece = 'шт.'


class Product:
    """Продукт"""

    def __init__(self):
        self.name = None
        self.price = None
        self.weight = None
        self.format = None

    @staticmethod
    def create_product_from_tuple(tup: tuple) -> 'Product':
        """Создает сущность продукта из специально подготовленного кортежа"""
        item = Product()
        item.name, item.price, item.weight, item.format = tup
        return item


class Buy(Product):
    """Позиция чека. Правильнее было бы назвать Position, но по условию задачи почему-то Buy"""

    def __init__(self):
        super().__init__()
        self.count = 0
        self.total_weight = 0.00
        self.total_price = 0.00

    def add_product(self, item: 'Product'):
        """Добавляет продукт к позиции"""
        self.weight = item.weight
        self.name = item.name
        self.price = item.price
        self.format = item.format
        self.inc_buy(item)

    def inc_buy(self, item: 'Product'):
        """Обновляет информацию о позиции: увеличивает общую стоимость позиции, вес, считает количество"""
        self.count += 1
        self.total_price += item.price * item.weight
        self.total_weight += item.weight


class Check(Buy):
    """Чек. Содержит список позиций"""

    def __init__(self):
        super().__init__()
        self.buy_list = set()

    def print(self):
        print("{:*^50}".format(" МАГНИТ НА ЧЕХОВА "))
        i = 0
        sum = 0
        for buy in self.buy_list:
            sum += buy.total_price
            i += 1
            print("{}. {} - {} руб./{} * {} == {}".format(
                i, buy.name, buy.price, buy.format, buy.weight, buy.total_price
            ))
        print("{:>40}{:>10}".format("Общая сумма покупки:", sum))
        print("{:*^50}".format(" Спасибо за покупку! "))

    def add_position(self, item: 'Product'):
        """Добавление продукта в позицию чека"""
        for buy in self.buy_list:
            if item.name == buy.name:
                buy.inc_buy(item)
                return
        buy = Buy()
        buy.add_product(item)
        self.buy_list.add(buy)


prod_list = [
    ('Сыр Пармезан', 600.00, 0.5, Format.kg),
    ('Яйца С1', 6.00, 10.0, Format.piece),
    ('Лейс', 50.00, 1, Format.piece),
    ('Яйца С2', 5.00, 20.0, Format.piece),
    ('Соль', 20.00, 2.0, Format.piece),
    ('Сыр Пармезан', 600.00, 0.7, Format.kg),
    ('Яйца С1', 6.00, 10.0, Format.piece),
    ('Батон', 20.00, 1.0, Format.piece),
    ('Батон', 20.00, 1.0, Format.piece),
    ('Молоко', 50.00, 2.0, Format.liter),
    ('Вареная колбаса', 400.00, 0.45, Format.kg),
    ('Крупа гречневая', 60.00, 3.0, Format.kg)
]

check = Check()
for prod in prod_list:
    product = Product.create_product_from_tuple(prod)
    check.add_position(product)
check.print()
