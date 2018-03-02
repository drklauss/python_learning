# Дан список чисел, который может содержать до 100000 чисел (каждое число от 0 до 1000).
# Определите, сколько в нем встречается различных чисел.
# Эту задачу на Питоне можно решить в одну строчку, но нам нужно с помощью словаря.

# Т.к. почти всегда в этой задаче количество значений равно 1001, то интересно было автоматизировать процесс
# получения другого набора. Т.е. у нас присутствует весь набор при таком количестве чисел.
# Решил автоматизировать подсчет и собрать некоторые статистические данные для других значений
import random
import time

ITERATIONS = 1000
SEQ_VAL_START = 0
SEQ_VAL_END = 10000
SEQUENCE_LEN = 100000


def calc_unique_nums() -> int:
    result = {}
    num_list = [random.randint(SEQ_VAL_START, SEQ_VAL_END) for _ in range(SEQUENCE_LEN)]
    for one_value in num_list:
        try:
            result[one_value] += 1
        except KeyError:
            result[one_value] = 1
    return len(result)


def get_unique_dict() -> dict:
    unique_dict = {}
    for v in range(0, ITERATIONS):
        uniq = calc_unique_nums()
        try:
            unique_dict[uniq] += 1
        except KeyError:
            unique_dict[uniq] = 1
    return unique_dict


def calc_probability(un_dict: dict):
    res = {}
    for k, v in un_dict.items():
        res[k] = "{:.2f}%".format(v / ITERATIONS * 100)
    return res


start = time.time()
dic = get_unique_dict()
print(calc_probability(dic))
end = time.time()
print("{} iterations time:{:.6f}".format(ITERATIONS, end - start))
