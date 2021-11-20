# author is Alyona Koryagina
# 16-11-2021
# python basics course
# lesson 6, exercise 2
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
# width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1
# см * чи сло см толщины полотна. Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def AsphaltMass(self, m3_mass=25, thickness=5):
        mass = format((self._width * self._length * m3_mass * thickness)/1000, '.0f')
        print(f'{mass} tons')


road_one = Road(width=20, length=5000)
road_one.AsphaltMass()
