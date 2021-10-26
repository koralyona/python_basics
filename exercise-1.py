# author is Alyona Koryagina
# python basics course
# lesson 1, exercise 1
# Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки
# и сохраните в переменные, затем выведите на экран.


number = 9
string = "abcdef"
print(number, string)
print(number * string + 'A')

user_number = input('print any number:')
print('OK')
print(type(user_number))
user_number=int(user_number)
print('new type is')
print(type(user_number))
print(5 * user_number)
user_string = input('print any symbols')
print('your string is ' + user_string)
print('The END')

