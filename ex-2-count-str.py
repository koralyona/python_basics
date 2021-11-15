# author is Alyona Koryagina
# 14-11-2021
# python basics course
# lesson 5, exercise 2
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('file-ex2-l5.txt') as file:
    content = file.readlines()
    str_num = len(content)
    print(f'String number is {str_num}')
    for index, one_str in enumerate(content):
        len_str = len(one_str.split())
        if len_str != 1:
            add_s = 's'
        else:
            add_s = ''
        print(f'String #{index+1} includes {len_str} word{add_s}')
