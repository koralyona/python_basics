# author is Alyona Koryagina
# 28-10-2021
# python basics course
# lesson 2, exercise 2
# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()

my_list_str = input('Print your list: ')
my_list = my_list_str.split(', ')
if len(my_list) == 1:
    my_list = my_list_str.split(',')
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 9]
# len_list = len(my_list)
for index, item in enumerate(my_list):
    ind_del = index % 2
    if index == len(my_list) - 1:
        break
    elif ind_del == 0:
        my_list.insert(index, my_list[index + 1])
        my_list.pop(index + 2)
    else:
        continue
print('New list is ', my_list)
