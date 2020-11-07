###################################################################################
#                             Лабораторная работа № 2                             #
###################################################################################
# Дисциплина: Проектирование, архитектура и конструирование программных средств   #
# Студент: Толкачев Е.Н.                                                          #
# Группа: ИВТ-416                                                                 #
# Вариант 8                                                                       #
###################################################################################
#                                     Задание                                     #
###################################################################################
# Написать программу, в которой описана иерархия классов:
# Геометрические фигуры (ромб, прямоугольник, эллипс). Реализовать методы вычисления
# площади и периметра фигуры. Продемонстрировать работу всех методов классов,
# предоставив пользователю выбор типа фигуры для демонстрации.
###################################################################################
import math

# Расстояние между двумя точками
def distance(x1: float, y1: float, x2: float, y2: float):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


# Класс "Точка"
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y



# Родительский класс "Фигура"
class Figure:
    def __init__(self):
        self.type = 'Не создана'
        self.points = []

    def square(self): return 0      # Вычисление площади фигуры
    def perimeter(self): return 0   # Вычисление периметра фигуры



# Класс: прямоугольник
class Rectangle(Figure):
    def __init__(self, first_point: Point, second_point: Point):
        self.points = []
        self.points.append(first_point)
        self.points.append(second_point)
        self.type = 'Прямоугольник'

    def square(self) -> float:
        x_max, x_min = (self.points[0].x, self.points[1].x) if (self.points[0].x > self.points[1].x) else (self.points[1].x, self.points[0].x)
        y_max, y_min = (self.points[0].y, self.points[1].y) if (self.points[0].y > self.points[1].y) else (self.points[1].y, self.points[0].y)
        figure_height = distance(x_min, y_min, x_min, y_max)
        figure_width = distance(x_min, y_min, x_max, y_min)
        return figure_height * figure_width

    def perimeter(self) -> float:
        x_max, x_min = (self.points[0].x, self.points[1].x) if (self.points[0].x > self.points[1].x) else (self.points[1].x, self.points[0].x)
        y_max, y_min = (self.points[0].y, self.points[1].y) if (self.points[0].y > self.points[1].y) else (self.points[1].y, self.points[0].y)
        figure_height = distance(x_min, y_min, x_min, y_max)
        figure_width = distance(x_min, y_min, x_max, y_min)
        return (figure_height * 2) + (figure_width * 2)



# Класс: ромб
class Rhombus(Figure):
    def __init__(self, first_point: Point, second_point: Point):
        self.points = []
        self.points.append(first_point)
        self.points.append(second_point)
        self.type = 'Ромб'

    def square(self):
        x_max, x_min = (self.points[0].x, self.points[1].x) if (self.points[0].x > self.points[1].x) else (self.points[1].x, self.points[0].x)
        y_max, y_min = (self.points[0].y, self.points[1].y) if (self.points[0].y > self.points[1].y) else (self.points[1].y, self.points[0].y)
        rhombus_width  = 2 * (distance(x_min, y_min, x_max, y_min))
        rhombus_height = 2 * (distance(x_max, y_max, x_max, y_min))
        return 0.5 * rhombus_width * rhombus_height

    def perimeter(self):
        x_max, x_min = (self.points[0].x, self.points[1].x) if (self.points[0].x > self.points[1].x) else (self.points[1].x, self.points[0].x)
        y_max, y_min = (self.points[0].y, self.points[1].y) if (self.points[0].y > self.points[1].y) else (self.points[1].y, self.points[0].y)
        return 4 * distance(x_min, y_min, x_max, y_max)



class Ellipse(Figure):
    def __init__(self, center_point: Point, semi_major_axis: float, semi_minor_axis: float):
        self.points = []
        self.points.append(center_point)
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis
        self.type = 'Эллипс'

    def square(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis

    def perimeter(self):
        return 4 * ((math.pi * self.semi_minor_axis * self.semi_major_axis) + (self.semi_major_axis - self.semi_minor_axis))/(self.semi_major_axis + self.semi_minor_axis)


point_1 = Point(0.0, 0.0)
point_2 = Point(4.0, 4.0)
my_rectangle = Rectangle(point_1, point_2)
print(f"Площадь прямоугольника: {my_rectangle.square()}")
print(f"Периметр прямоугольника: {my_rectangle.perimeter()}")

point_3 = Point(0.0, 0.0)
point_4 = Point(2.0, 4.0)
my_rhombus = Rhombus(point_3, point_4)
print(f"Площадь ромба: {my_rhombus.square()}")
print(f"Периметр ромба: {my_rhombus.perimeter()}")


point_5 = Point(0.0, 0.0)
ellipse_major_axis = 12
ellipse_minor_axis = 5
my_ellipse = Ellipse(point_5, ellipse_major_axis, ellipse_minor_axis)
print(f"Площадь эллипса: {my_ellipse.square()}")
print(f"Периметр эллипса: {my_ellipse.perimeter()}")