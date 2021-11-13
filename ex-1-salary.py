# author is Alyona Koryagina
# 13-11-2021
# python basics course
# lesson 4, exercise 1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv
if len(argv) < 4:
    print("Not all required parameters have been entered. Enter 3 parameters: output, wage rate and bonus")
    exit()
else:
    output = float(argv[1])
    wage_rate = float(argv[2])
    bonus = float(argv[3])


def salary(o, wg, b):
    result = (o * wg) + b
    return result


print(f'Salary is {salary(output, wage_rate, bonus)}')
