# author is Alyona Koryagina
# 20-11-2021
# python basics course
# lesson 6, exercise 5
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для
# каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def method_draw(self):
        print('Start drawing')


class Pen(Stationery):
    def method_draw(self):
        super().method_draw()
        print(f'Drawing with pen {self.title}')


class Pencil(Stationery):
    def method_draw(self):
        super().method_draw()
        print(f'Drawing with pencil {self.title}')


class Handle(Stationery):
    def method_draw(self):
        super().method_draw()
        print(f'Drawing with handle {self.title}')


pen = Pen('A')
pen.method_draw()
pencil = Pencil('B')
pencil.method_draw()
handle = Handle('C')
handle.method_draw()