# Задача: В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно
# и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных
# числа: количество учащихся в каждом из трех классов.


firstClass = int(input('В первом классе: '))
secondClass = int(input('Во втором классе: '))
thirdClass = int(input('В третьем классе: '))
firstClassDesks = firstClass % 2 + firstClass // 2
secondClassDesks = secondClass % 2 + secondClass // 2
thirdClassDesks = thirdClass % 2 + thirdClass // 2
print('Первый класс: \r\nУченики: {} \r\nПарты: {}'.format(firstClass, firstClassDesks))
print('Второй класс: \r\nУченики: {} \r\nПарты: {}'.format(secondClass, secondClassDesks))
print('Третий класс: \r\nУченики: {} \r\nПарты: {}'.format(thirdClass, thirdClassDesks))
