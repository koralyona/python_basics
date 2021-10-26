# author is Alyona Koryagina
# python basics course
# lesson 1, exercise 5
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее
# сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

ret = float(input('Print returns: '))
costs = float(input('Print costs: '))

if costs < ret:
    print('You have profit')
    profit = ret - costs
    print(f'Your profit is {profit}')
    profitability = 100 * (profit / ret)
    print(f'Your profitability is {profitability}%')
    emp_num = int(input('Print number of employees: '))
    emp_profit = profit / emp_num
    print(f'Profit for one employee is {emp_profit}')
elif costs == ret:
    print("You don't have profit")
else:
    print('You have loss')
