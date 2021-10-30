# author is Alyona Koryagina
# 28-10-2021
# python basics course
# lesson 2, exercise 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
# одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
print(f'old list {my_list}')
el = int(input('Print new element: '))
last_index = len(my_list)-1
for index, item in enumerate(my_list):
    if el > item:
        my_list.insert(index, el)
        break
    elif el < my_list[last_index]:
        my_list.append(el)
        break
    else:
        continue
print(f'new list {my_list}')
