# author is Alyona Koryagina
# 14-11-2021
# python basics course
# lesson 5, exercise
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus_dict = {'Один': 1, 'Два': 2, 'Три': 3, 'Четыре': 4}

with open('file-ex4-l5.txt') as file_read, open('file-ex4-l5-2.txt', 'w') as file_write:
    file_read.seek(0)
    content = file_read.readlines()
    for item in content:
        one_str = item.split('—')
        num = int(one_str[1])
        for key, value in rus_dict.items():
            if num == value:
                file_write.writelines(f'{key} - {num}\n')
    print('New file created')

