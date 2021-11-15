# author is Alyona Koryagina
# 15-11-2021
# python basics course
# lesson 5, exercise 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import random

file_name = 'file-ex5-l5.txt'
with open(file_name, 'w+') as file:
    # Creation of random numbers to file
    n = 0
    while n < 20:
        n += 1
        some_num = format(random()*100, '.1f')
        file.writelines(f'{some_num} ')

    # Read content in file and sum numbers
    file.seek(0)
    content = file.readline()
    num_sum = 0
    for i in content.split():
        num_sum += float(i)

print(f"Sum of numbers in {file_name} is {format(num_sum, '.1f')}")
