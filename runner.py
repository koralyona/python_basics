# author is Alyona Koryagina
# python basics course
# lesson 1, exercise 6
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер
# дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.

km_1_day = int(input('How many kilometres does sportsman run in first day? '))
km_result = int(input('How many kilometres should sportsman run? '))
km = km_1_day
day = 1
while km < km_result:
    km = km * 1.1
    day = day + 1
print(f'Sportsman will run minimum {km_result} kilometres on {day} day')