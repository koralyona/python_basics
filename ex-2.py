# author is Alyona Koryagina
# 06-11-2021
# python basics course
# lesson 3, exercise 2
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать
# вывод данных о пользователе одной строкой.

def person_data(birth_year, residence_city, email, tel_number, person_name, person_surname):
    """Принимает данные пользователя, возвращает все данные в одной строке"""
    result = print(f'{person_name} {person_surname} {birth_year} {residence_city} {email} {tel_number}')
    return result


name = input('Your name: ')
surname = input('Your surname: ')
tel = input('Your telephone number: ')
city = input('Your city of residence: ')
year = input('Your birth year: ')
em = input('Your e-mail: ')

person_data(birth_year=year, residence_city=city, email=em, tel_number=tel, person_name=name, person_surname=surname)
