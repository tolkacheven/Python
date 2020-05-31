"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
import random
import time

class TrafficLight:
    __traffic_light_colors   = ['green', 'yellow', 'red']       # Цвета светофора;

    __traffic_light_sequence = {'green':  'yellow',             # Последовательность цветов;
                                'yellow': 'red',
                                'red':    'green'}

    __traffic_light_duration = {'green':  5,                    # Продолжительность зеленого сигнала
                                'yellow': 2,                    # Продолжительность желтого сигнала
                                'red':    7}                    # Продолжительность красного сигнала

    __color = ''                                                # Текущий цвет


    # Конструктор
    # Аргумент start_color: начальный цвет светофора, без указания задается случайно;
    # Аргумент green_light_duration: продолжительность зеленого света (по умолчанию 5).
    def __init__(self, start_color = random.choice(__traffic_light_colors), green_light_duration = 5):
        self.__color = start_color
        self.__traffic_light_duration[self.__color] = int(green_light_duration)

    # Метод запуска светофора
    def running(self):
        print(f'Стартовый цвет: {self.__color}')
        current_light = self.__color
        previous_light = current_light

        while True:
            print(f'{current_light}')
            time.sleep(self.__traffic_light_duration.get(current_light))
            previous_light = current_light
            current_light  = self.__traffic_light_sequence.get(current_light)

            # Проверка порядка режимов
            if self.__traffic_light_sequence[previous_light] != current_light:
                print('Ошибка: последовательность нарушена')
                break


traffic_light_test = TrafficLight()
traffic_light_test.running()