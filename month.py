# author is Alyona Koryagina
# 28-10-2021
# python basics course
# lesson 2, exercise 3
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

# # если вводить название месяца
# mon = input('Print month: ')
# month_str = 'january, february, march, april, may, june, july, august, september, october, november, december'
# month_list = month_str.split(', ')
# mon_num = month_list.index(mon)+1

mon_num = int(input('Print month number: '))

if mon_num > 12:
    print(f'There is no month with #{mon_num}')
    exit()

# если использовать словарь
month_dict = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
for key, value in month_dict.items():
    for item in value:
        if item == mon_num:
            print(f'This is {key}')
        else:
            continue

# если использовать list
month_list = [0, 'winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn',
              'autumn', 'autumn', 'winter']
print(f'This is {month_list[mon_num]}')
