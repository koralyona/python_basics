# author is Alyona Koryagina
# 14-11-2021
# python basics course
# lesson 5, exercise 3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

with open('file-ex3-l5.txt') as file:
    content = file.readlines()
    sal_sum = 0
    for item in content:
        one_person = item.split()
        one_person_sn = one_person[0]
        one_person_sal = float(one_person[1])
        sal_sum += one_person_sal
        if one_person_sal < 20000:
            print(one_person_sn)
        else:
            continue
    average_sal = sal_sum/len(content)
    print(f'Average salary is {average_sal}')


