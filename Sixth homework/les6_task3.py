"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    ################
    ##  Атрибуты  ##
    ################
    name     = ''
    surname  = ''
    position = ''
    _income  = {'wage': 0, 'bonus': 0}

    def set_income(self, wage = 0, bonus = 0):
        self._income['wage']  = wage
        self._income['bonus'] = bonus


class Position(Worker):
    ################
    ##   Методы   ##
    ################

    # Получить полное имя сотрудника
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    # Получить доход сотрудника с учетом премии
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker = Position()
worker.set_income(100000, 20000)
worker.name = 'John'
worker.surname = 'Doe'
worker.position = 'Janitor'

print(f'Имя сотрудника: {worker.get_full_name()}')
print(f'Доход: {worker.get_total_income()}')