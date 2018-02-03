# Посчитать количество слов в введёном с клавиатуры предложении.

text = input('Введите предложение: ')

wordsCount = 0
isPreLastAlpha = False
for letter in text:
    isAlpha = letter.isalpha()
    if not isAlpha and isPreLastAlpha:
        wordsCount += 1
    isPreLastAlpha = isAlpha
print('Слов в предложении: ', wordsCount)

