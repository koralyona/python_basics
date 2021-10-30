# author is Alyona Koryagina
# 28-10-2021
# python basics course
# lesson 2, exercise 4
# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

my_str = input('Print your string: ')
my_list = my_str.split()
for index, item in enumerate(my_list):
    print(f'{index+1} - {item[:10]}')
