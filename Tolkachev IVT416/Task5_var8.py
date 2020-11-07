###################################################################################
#                             Лабораторная работа № 5                             #
###################################################################################
# Дисциплина: Проектирование, архитектура и конструирование программных средств   #
# Студент: Толкачев Е.Н.                                                          #
# Группа: ИВТ-416                                                                 #
# Вариант 8                                                                       #
###################################################################################
#                                     Задание                                     #
###################################################################################
# Нарисовать график функции (ax3+bx2+cx+d)sin(x^2)
# #################################################################################
import matplotlib.pyplot as plt
import math

class Function:
    def __init__(self, a: float, b: float, c: float, d: float, x_from: float, x_to: float, accuracy = 0.1):
        self.a, self.b, self.c, self.d = a, b, c, d
        self.x_from = x_from
        self.x_to = x_to
        self.accuracy = accuracy
        self.x = []
        self.y = []

    def f(self, x: float) -> float:
        return (self.a * pow(x, 3) + self.b * pow(x,2) + self.c * x + self.d)*math.sin(pow(x, 2))

    def build(self):
        self.x = []
        self.y = []
        range_from = self.x_from
        while (range_from <= self.x_to):
            self.x.append(range_from)
            self.y.append(self.f(self.x[len(self.x)-1]))
            range_from += self.accuracy

    def draw(self):
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('(ax3+bx2+cx+d)sin(x^2)')
        plt.plot(self.x, self.y)
        plt.show()


func_1 = Function(1, 0, 0, 0, -1, 3, 0.1)
func_1.build()

func_2 = Function(2, 1, 1, 0, -1, 3, 0.01)
func_2.build()

plt.plot(func_1.x, func_1.y, label='x3 * sin(x^2)')
plt.plot(func_2.x, func_2.y, label='2x3 + x2 + x')

plt.legend()
plt.show()

