# author is Alyona Koryagina
# 15-11-2021
# python basics course
# lesson 5, exercise 7
# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

with open('file-ex7-l5.txt') as open_file, open('result-ex7-l5.json', 'w') as res_file:
    content = open_file.readlines()

    profit_dict = {}
    loss_dict = {}
    av_profit_dict = {}
    sum_profit = 0

    for item in content:
        # Firm name
        firm_name = item.split()[0]
        result = int(item.split()[2]) - int(item.split()[3])
        if result > 0:
            profit = result
            sum_profit += profit
            profit_dict[firm_name] = profit
        elif result < 0:
            loss = result
            loss_dict[firm_name] = loss
        else:
            continue

    average_profit = sum_profit/len(content)
    av_profit_dict['average_profit'] = average_profit

    firm_list = [profit_dict, av_profit_dict, loss_dict]
    json.dump(firm_list, res_file)
    print('.json file created')
