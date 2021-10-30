# author is Alyona Koryagina
# 28-10-2021
# python basics course
# lesson 2, exercise 1
# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а
# указать явно, в программе

my_list = [1, -2, 3.2, 'text', None, True, (4, 5, 6, None), True]
print(f'length of list is {len(my_list)}')
# # my_list.append(False)
# # print(my_list[(len(my_list))-1])
# # my_list.remove(False)
# # print(my_list)
my_list.insert(4, [2, 17, 'dog'])
# # print(len(my_list))
# for item in my_list:
#     print(item, type(item))
print('index - item - type of item')
for index, item in enumerate(my_list):
    print(f'{index} - {item} - {type(item)}')
