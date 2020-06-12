"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, input_matrix: list):
        self.__data = input_matrix
        self.__dimension = len(self.__data[0])  # Предполагается, что матрица квадратная. Учту способ с поиском
                                                            # максимальной длины;

    # Порядок матрицы
    @property
    def dimension(self):
        return self.__dimension

    def item(self, i: int, j: int):
        return self.__data[i][j]


    def __str__(self):
        result = ''
        for row in self.__data:
            for element in row:
                result += " {:4d} ".format(element)
            result += '\n'
        return result


    def __add__(self, other):
        result = []
        if self.dimension != other.dimension:
            print('Ошибка: матрицы разных порядков')
            return
        for i in range(self.dimension):
            result.append([])
            for j in range(self.dimension):
                result[i].append(self.item(i, j) + other.item(i, j))

        return Matrix(result)


first_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second_matrix = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print(first_matrix)
print(second_matrix)

print(first_matrix.dimension)
print(second_matrix.dimension)

third_matrix = first_matrix + second_matrix

print(third_matrix)
