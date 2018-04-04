inp = """
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I
"""

lines = inp.split("\n")

children = {}
parents = {}
kaiser = ""  # самый главнюк
for line in lines:
    names = line.split()
    if len(names) == 2:
        parent = names[1]
        child = names[0]
        # определяем у кого кто родитель
        parents[child] = parent
        # главнюка
        if kaiser == "" or parent not in parents:  # главнюка ещё не определили и тогда берём первого попавшегося человека или берем того, у кого нет родителей
            kaiser = parent
        # записываем кто кого родил
        if parent not in children:
            children[parent] = [child]
        else:
            children[parent].append(child)

people_levels = {kaiser: 0}  # первым вставляем главнюка
if len(children) == 0:  # если детей никто не имел, то и дело с концом
    print(people_levels)
    exit()


# функция выставляет уровень всем детям
def set_level_to_children(parent: str):
    level = people_levels[parent] + 1  # вычисляем уровень детей по уровню родителя
    for child in children[parent]:
        people_levels[child] = level
        if child in children:  # если ребёнок сам был родителем
            set_level_to_children(child)


set_level_to_children(kaiser)

list_for_sort = [(man, level) for man, level in people_levels.items()]

list_for_sort.sort()

print(list_for_sort)