# author is Alyona Koryagina
# 13-11-2021
# python basics course
# lesson 4, exercise 6
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором
# также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count

# a) Генерируется список из целых чисел, начиная с заданного пользователем до 100
init_num = int(input('Print one integer number: '))
integer_list = []
break_num = 100
while init_num > break_num:
    init_num = int(input(f'Print integer number less then {break_num}: '))

for i in count(init_num):
    if i > break_num:
        break
    else:
        integer_list.append(i)

print(f'List of integer numbers from {init_num} to {break_num}: {integer_list}')
