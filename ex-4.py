# author is Alyona Koryagina
# 07-11-2021
# python basics course
# lesson 3, exercise 4
# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй —
# более сложная реализация без оператора **, предусматривающая использование цикла.

x = float(input('Print positive number: '))
y = int(input('Print negative integer number: '))


def my_func(x, y):
    result = x**y
    return result


print(f'Result with ** operator: {my_func(x, y)}')


def my_func_2(x, y):
    y = abs(y)
    if y == 1:
        result = 1/x
    else:
        new_x = x
        for elem in range(y-1):
            new_x = 1 / (new_x * x)
        result = new_x
    return result


print(f'Result with cycle: {my_func_2(x, y)}')
