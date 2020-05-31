"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:
    ################
    ##  Атрибуты  ##
    ################
    _length = 0
    _width  = 0

    ################
    ##   Методы   ##
    ################
    def __init__(self, input_length = 0, input_width = 0):
        self._length = input_length
        self._width  = input_width


    def calculate_asphalt_weight(self, asphalt_one_meter_weight = 0.0, asphalt_depth = 0.0):
        return self._width * self._length * asphalt_one_meter_weight * asphalt_depth


some_road = Road(20, 5000)
asphalt_total_mass = some_road.calculate_asphalt_weight(25, 5)

print(f'{asphalt_total_mass/1000} т.')
