# author is Alyona Koryagina
# 21-11-2021
# python basics course
# lesson 7, exercise 1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

from tabulate import tabulate


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        matrix_view = tabulate(self.data, tablefmt='plain')
        return f'{matrix_view}\n'

    # def __str__(self):
    #     matr = ''
    #     for i in self.data:
    #         line = ''
    #         for ii in i:
    #             line += f' {ii:02} '
    #         matr += f'{line}\n'
    #     return matr

    def __add__(self, other):
        new_matr = []
        for ind_1, i in enumerate(self.data):
            new_line = []
            for ind_2, ii in enumerate(i):
                new_el = ii + other.data[ind_1][ind_2]
                new_line.append(new_el)
            new_matr.append(new_line)
        new_matrix = Matrix(new_matr)
        return new_matrix


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
