"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, name: str):
        self.__name = name

    @abstractmethod
    def calculate_amount_of_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, name: str, size: int):
        self.__size = size
        super().__init__(name)

    @property
    def size(self):
        return self.__size

    def calculate_amount_of_cloth(self):
        return self.size/6.5 + 0.5

class Costume(Clothes):
    def __init__(self, name, height):
        self.__height = height
        super().__init__(name)

    @property
    def height(self):
        return self.__height

    def calculate_amount_of_cloth(self):
        return 2 * self.height + 0.3


coat_test = Coat('Пальто', 48)
costume_test = Costume('Костюм', 50)

print(coat_test.size)
print(costume_test.height)

print(coat_test.calculate_amount_of_cloth())
print(costume_test.calculate_amount_of_cloth())