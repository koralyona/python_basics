# author is Alyona Koryagina
# 15-11-2021
# python basics course
# lesson 5, exercise 6
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.

with open('file-ex6-l5.txt') as file:
    content = file.readlines()
    subj_dict = {}
    for item in content:
        # Find subject name
        subject = item.split()[0]
        subject_new = ''
        # Delete ':' in subject name
        for char in subject:
            if char.isalpha():
                subject_new += char
            else:
                continue
        # Subject name is
        # print(subject_new)

        # Find hours
        h_list = []
        for i in item.split():
            h = ''
            for char in i:
                if char.isdigit():
                    h += char
                else:
                    continue
            h_list.append(h)
        # Get rid of empty values
        h_sum = 0
        for i in h_list:
            if i.isdigit():
                h_sum += int(i)
            else:
                continue
        # Sum of hours is
        # print(h_sum)

        # Add subject as key in dict and sum of hours as value
        subj_dict[subject_new] = h_sum
    print(subj_dict)
