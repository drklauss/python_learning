# Посчитать количество слов в введёном с клавиатуры предложении.

text = input('Введите предложение: ')

words_count = 0
isPreLastAlpha = False
for letter in text:
    isAlpha = letter.isalpha()
    if not isAlpha and isPreLastAlpha:
        words_count += 1
    isPreLastAlpha = isAlpha
print('Слов в предложении: ', words_count)

