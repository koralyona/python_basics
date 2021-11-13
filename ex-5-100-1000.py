# author is Alyona Koryagina
# 13-11-2021
# python basics course
# lesson 4, exercise 5
# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)
print(reduce(lambda n_1, n_2: n_1 * n_2, my_list))
