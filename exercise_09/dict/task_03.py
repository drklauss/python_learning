# Выведите все слова, встречающиеся в тексте, по одному на каждую строку. Слова должны быть отсортированы по убыванию
# их частоты появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке. Указание.
# После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
# Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов:
# частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
# Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу,
# а если они равны — то по второму. Это почти то, что требуется в задаче.

import re

phrase = """Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille
         Buonaparte. Non, je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous
         permettez encore de pallier toutes les infamies, toutes les atrocités de cet Antichrist
         (ma parole, j'y crois) — je ne vous connais plus, vous n'êtes plus mon ami, vous n'êtes plus
         мой верный раб, comme vous dites"""


def get_words_count(phr: str) -> dict:
    """Возвращает подсчитанное количество слов в тексте"""
    words_dict = {}
    words = re.findall("[\w|']{2,}", phr)  # собираем все слова, состоящие из Юникод-символов от 2х букв
    for word in words:
        try:
            words_dict[word] += 1
        except KeyError:
            words_dict[word] = 1
    return words_dict


def nice_print(res: dict):
    """Выводит список встречающихся слов в лексиграфическом порядке с указанием встречаемости слова"""
    sorted_list_of_tuples = sorted(res.items(), key=lambda x: (x[1], x[0]))
    for tup in sorted_list_of_tuples:
        print("{} - {}".format(tup[0], tup[1]))


result = get_words_count(phrase)
nice_print(result)
