# author is Alyona Koryagina
# 07-11-2021
# python basics course
# lesson 3, exercise 3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

nums_str = input('Print 3 numbers: ')
nums_list = nums_str.split()
n_1 = int(nums_list[0])
n_2 = int(nums_list[1])
n_3 = int(nums_list[2])


def my_func(num_1, num_2, num_3):
    num_sum = num_1 + num_2 + num_3 - min(num_1, num_2, num_3)
    return num_sum


print(my_func(n_1, n_2, n_3))
