# author is Alyona Koryagina
# 14-11-2021
# python basics course
# lesson 5, exercise 1
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('file-ex1-l5.txt', 'w') as file:
    finished = False
    while not finished:
        content = input('Print content: ')
        if content == '':
            finished = True
        else:
            file.writelines(f'{content}\n')

