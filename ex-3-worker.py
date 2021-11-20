# author is Alyona Koryagina
# 16-11-2021
# python basics course
# lesson 6, exercise 3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def total_income(self):
        t_i = int(self._income['wage']) + int(self._income['bonus'])
        print(f'Total income is {t_i}')


person = Position('Ivan', 'Ivanov', 'manager', '50000', '5000')
print(person.name)
print(person.surname)
print(person.position)
print(person._income)
person.get_full_name()
person.total_income()
