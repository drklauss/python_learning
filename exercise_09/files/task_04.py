# С помощью словаря из файла codes.txt расшифровать текст
# 006005034028017006029034028017006006017036034028020021029034028017028017
import re
import sys


def get_line() -> iter:
    """Возвращает итератор строк"""
    with open(sys.argv[1]) as f:
        for line in f:
            yield line


def generate_dict() -> dict:
    """Создает и возвращает словарь для декодирования"""
    codes_dict = {}
    re_compile = re.compile("(\w|\W)\s(\d{3})")
    for ln in get_line():
        ls = re.findall(re_compile, ln).pop()
        codes_dict[ls[1]] = ls[0]
    return codes_dict


def decode_text(txt: str, codes_dict: dict) -> list:
    """Возвращает список декодированных символов"""
    chars_encoded = re.findall("\d{3}", txt)
    result = []
    for char in chars_encoded:
        try:
            result.append(codes_dict[char])
        except KeyError:
            result.append("err")
            continue
    return result


enc_phrase = "006005034028017006029034028017006006017036034028020021029034028017028017"
txt_dec = decode_text(enc_phrase, generate_dict())
print(''.join(txt_dec))
