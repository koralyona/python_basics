# author is Alyona Koryagina
# 06-11-2021
# python basics course
# lesson 3, exercise 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(divid, divis):
    """Принимает значения делимого и делителя, возвращает частное"""
    if divis == 0:
        print('Division by 0 is impossible')
    else:
        result = divid / divis
        return result


dd = float(input('print divident: '))
ds = float(input('print divisor: '))

print(division(dd, ds))
