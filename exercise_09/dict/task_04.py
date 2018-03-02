# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
# У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам дано генеалогическое древо, определите высоту всех его элементов.

tree = "Alexei Peter_I\n\
Anna Peter_I\n\
Elizabeth Peter_I\n\
Peter_II Alexei\n\
Peter_III Anna\n\
Paul_I Peter_III\n\
Alexander_I Paul_I\n\
Nicholaus_I Paul_I"


def init_pairs(pairs_str: str) -> []:
    pairs = pairs_str.split(sep="\n")
    pairs_list = []
    for pair in pairs:
        tup = pair.split(" ")
        try:
            pairs_list.append({tup[0]: tup[1]})
        except IndexError:
            continue
    return pairs_list


def create_tree(pairs: []):
    tree = []
    for pair in pairs:
        child, parent = pair.popitem()
        parent_found = False
        key = -1
        while key > -1:
            key, item = get_parent(tree, parent)
            tree[key][2] += 1
            parent_found = True
        # break
        if not parent_found:
            tree.append([parent, "", 0])


def get_parent(tree: [], parent: str):
    for item in tree:
        if parent == item[1]:
            return tree.index(item), item
    return -1, ""


init_pairs(tree)
