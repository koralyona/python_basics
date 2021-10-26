# author is Alyona Koryagina
# python basics course
# lesson 1, exercise 2
# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк

print('This is convector of seconds')
user_sec = int(input('Print number of seconds: '))
if user_sec < 0:
    print("Number of seconds can't be less than zero.")
else:
    #    print(user_seq, 'seconds')
    seconds = user_sec % 60
    ss = seconds
    minutes = user_sec // 60
    mm = minutes % 60
    hours = minutes // 60
    if hours < 24:
        hh = hours
    else:
        hh = hours % 24
        days = hours // 24
        dd = days
        if dd == 1:
            print(f'{dd} day')
        else:
            print(f'{dd} days')
    time = f'{hh:02}:{mm:02}:{ss:02}'
    print(time)
# print('Program is over')
