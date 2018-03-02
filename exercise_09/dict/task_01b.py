# Создать словарь из слов, которые введёт пользователь.
# Ключи - слова, значения - их порядок расположения в исходном тексте.
#  Например, текст я понял, что эти так быстро проходят. Словарь получится:
import re

phrase = input('Введите фразу:')
words = re.findall('[а-яА-я]+', phrase)
position = 0
result = {}
for word in words:
    position += 1
    result[word] = position
print(result)
