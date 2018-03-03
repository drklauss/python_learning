# Программа должна подсчитать количество строк, слов и букв в переданном ей файле.
# Имя файла должно передаваться в качестве первого аргумента после имени самого скрипта.
# Например, вызов скрипта в Linux через командную оболочку выглядит примерно так:
# python3 words.py text.txt

import sys


def get_line() -> iter:
    """Возвращает итератор строк"""
    with open(sys.argv[1]) as f:
        for line in f:
            yield line


def get_counters() -> tuple:
    """Возвращает подсчитанное количество строк, слов и букв в тексте"""
    words_count = 0
    letters_count = 0
    lines_count = 0
    for ln in get_line():
        lines_count += 1
        is_pre_last_alpha = False
        for letter in ln:
            is_alpha = letter.isalpha()
            letters_count += 1 if is_alpha else 0
            if not is_alpha and is_pre_last_alpha:
                words_count += 1
            is_pre_last_alpha = is_alpha
    return lines_count, words_count, letters_count


print("Строк: {}\nСлов: {}\nБукв: {}".format(*get_counters()))

