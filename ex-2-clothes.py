# author is Alyona Koryagina
# 21-11-2021
# python basics course
# lesson 7, exercise 2
# Реализовать проект расчета
# суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может
# иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
# существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return f'{self.size/6.5 + 0.5}'


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def fabric_consumption(self):
        return f'{2 * self.height + 0.3}'


def sum_consumption(list_clothes):
    s = 0
    for i in list_clothes:
        s += float(i.fabric_consumption)
    return s


coat_1 = Coat(50)
print(coat_1.fabric_consumption)
suit_1 = Suit(1.8)
print(suit_1.fabric_consumption)
list_clothes = [coat_1, suit_1]
print(sum_consumption(list_clothes))
