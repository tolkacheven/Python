"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
# Класс "автомобиль"
class Car:
    ################
    ##  Атрибуты  ##
    ################
    speed = 0
    color = ''
    name  = ''
    is_police = False

    ################
    ##   Методы   ##
    ################
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def display_info(self):
        print(f'{self.name}, {self.color}, speed: {self.speed}')


# Легковая машина
class TownCar(Car):
    speed = 40

    def show_speed(self):
        if self.speed > 60:
            print(f'Скоростной лимит превышен. {self.speed} при разрешенных 60!')
        else:
            print(f'Текущая скорость: {self.speed}')


# Рабочая машина
class WorkCar(Car):
    speed = 30

    def show_speed(self):
        if self.speed > 40:
            print(f'Скоростной лимит превышен. {self.speed} при разрешенных 40!')
        else:
            print(f'Текущая скорость: {self.speed}')


# Спортивная машина
class SportCar(Car):
    speed = 210


# Полицейская машина
class PoliceCar(Car):
    speed = 80
    is_police = True

    def signal(self):
        print('Виу-виу-виу')


# Городская машина
towncar = TownCar()
towncar.name  = 'Ford Crown Victoria'
towncar.color = 'Grey'
towncar.display_info()
towncar.show_speed()
towncar.speed = 61
towncar.show_speed()


# Рабочая машина
workcar = WorkCar()
workcar.name  = 'Caterpillar D7'
workcar.color = 'Yellow'
workcar.display_info()
workcar.show_speed()
workcar.speed = 41
workcar.show_speed()


# Спортивная машина
sportcar = SportCar()
sportcar.name  = 'Lamborghini Aventador'
sportcar.speed = 320
sportcar.color = 'Orange'
sportcar.display_info()


# Полицейская машина
policecar = PoliceCar()
policecar.name  = 'Ford Police Interceptor Utility Hybrid SUV'
policecar.speed = 120
policecar.color = 'Black'
policecar.display_info()