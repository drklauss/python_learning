# Создать словарь из слов, которые введёт пользователь.
# Ключи - слова, значения - их порядок расположения в исходном тексте.
#  Например, текст я понял, что эти так быстро проходят. Словарь получится:

position = 0
dict_words = {}
while True:
    try:
        position += 1
        dict_words[input('Введите слово: ')] = position

    except EOFError:
        print(dict_words)
        exit(1)
