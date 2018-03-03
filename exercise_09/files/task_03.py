# Сделать задачу 3 по словарям с текстом из файла song.txt


import re
import sys


def get_line() -> iter:
    """Возвращает итератор строк"""
    with open(sys.argv[1]) as f:
        for line in f:
            yield line


def get_words_count() -> dict:
    """Возвращает подсчитанное количество слов в тексте"""
    words_dict = {}
    re_compile = re.compile("[\w|']{2,}")
    for ln in get_line():
        words = re.findall(re_compile, ln)  # собираем все слова, состоящие из Юникод-символов от 2х букв
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


w_dict = get_words_count()
nice_print(w_dict)
