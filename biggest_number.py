# author is Alyona Koryagina
# python basics course
# lesson 1, exercise 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения
# используйте цикл while и арифметические операции.

user_num = int(input('Print positive integer number: '))
big_num = 0
num_1 = user_num % 10
while user_num >0:
    if num_1 >= big_num:
        big_num = num_1
        user_num = user_num // 10
        num_1 = user_num % 10
    else:
        user_num = user_num // 10
        num_1 = user_num % 10
print(f'The biggest number is {big_num}')
