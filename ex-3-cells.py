# author is Alyona Koryagina
# 21-11-2021
# python basics course
# lesson 7, exercise 3
# Реализовать программу работы с органическими
# клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству
# клеток (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (
# __add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
# соответственно. В методе деления должно осуществляться округление значения до целого числа. Сложение. Объединение
# двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток. Вычитание.
# Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение. Умножение. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как произведение количества ячеек этих двух клеток. Деление. Создается общая клетка из двух. Число
# ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток. В классе необходимо
# реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет
# организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
# между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
# все оставшиеся. Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек в ряду —
# 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num

    def __add__(self, other):
        new_cell_num = self.cell_num + other.cell_num
        new_cell = Cell(new_cell_num)
        return f'{new_cell.cell_num}'

    def __sub__(self, other):
        if self.cell_num < other.cell_num:
            return f'Number of cells in first Cell is less then in second one. Subtraction is impossible.'
        else:
            new_cell = Cell(self.cell_num - other.cell_num)
            return f'{new_cell.cell_num}'

    def __mul__(self, other):
        new_cell_num = self.cell_num * other.cell_num
        new_cell = Cell(new_cell_num)
        return f'{new_cell.cell_num}'

    def __truediv__(self, other):
        new_cell = Cell(self.cell_num // other)
        return new_cell.cell_num

    def make_order(self, num_in_row):
        a, b = divmod(self.cell_num, num_in_row)
        in_order = ""
        for i in range(a):
            in_order += f"{num_in_row * '*'}\n"
        if b != 0:
            in_order += f"{b * '*'}\n"
        return in_order


cells_1 = Cell(20)
cells_2 = Cell(10)
# make order
print(cells_1.make_order(11))
# div
print(cells_1 / 3)
# add
print(cells_1 + cells_2)
# sub
print(cells_1 - cells_2)
print(cells_2 - cells_1)
# mull
print(cells_1 * cells_2)
