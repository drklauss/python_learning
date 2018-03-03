# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
# У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам дано генеалогическое древо, определите высоту всех его элементов.


def init_data() -> []:
    """Вычитывает входную строку в пары ребенок-родитель"""
    pairs = ls.split(sep="\n")
    for pair in pairs:
        tup = pair.split(" ")
        try:
            pairs_list.append({tup[0]: tup[1]})
        except IndexError:
            continue


def set_zero_men():
    """Устанавливает членов древа с нулевой высотой"""
    children = set()
    parents = set()
    for pair in pairs_list:
        for child, parent in pair.items():
            children.add(child)
            parents.add(parent)
    for zero_man in parents.difference(children):
        tree[zero_man] = 0


def fill_tree():
    """Заполняет дерево, выставляя каждому родителю его высоту"""
    for pair in pairs_list:
        for child in pair.keys():
            tree[child] = get_height_recursively(child, 0)


def get_height_recursively(child: str, height: int) -> int:
    """Рекурсивно вычисляет высоту человека"""
    try:
        parent = get_parent_by_child(child)
        return get_height_recursively(parent, height + 1)
    except KeyError:
        return height


def get_parent_by_child(child: str):
    """Возвращает родителя по ребенку. Если ребенок не найден, пробрасывает исключение выше"""
    for pair in pairs_list:
        try:
            return pair[child]
        except KeyError:
            continue
    raise KeyError


def nice_print():
    """Выводит список в отсортированном лексиграфическом порядке с указанием высоты"""
    for tup in sorted(tree.items(), key=lambda x: x[0]):
        print("{} - {}".format(tup[0], tup[1]))


ls = """Anna Peter_I
Paul_I Peter_III
Peter_III Anna
Alexander_I Paul_I
Alexei Peter_I
Elizabeth Peter_I
Peter_II Alexei
Nicholaus_I Paul_I"""
pairs_list = []
tree = {}


init_data()
set_zero_men()
fill_tree()
nice_print()
