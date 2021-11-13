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

from itertools import cycle

# b)
init_list = [300, 'A', 12]
final_list = []
z = 0
for el in cycle(init_list):
    if z > 30:
        break
    else:
        final_list.append(el)
        z += 1

print(final_list)
