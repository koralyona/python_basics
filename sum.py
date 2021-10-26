# author is Alyona Koryagina
# python basics course
# lesson 1, exercise 4
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_number = (input('Print your number: '))
n_str = user_number
num_sum = int(user_number) + int(2*user_number) + int(3*user_number)
print(f'Sum is {num_sum}')
