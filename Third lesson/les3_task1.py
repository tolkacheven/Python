"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError as error:
        print(f'Ошибка: знаменатель не может быть отрицательным ({error})')


print(division(2, 4))
print(division(4, 2))
print(division(5, 5))
print(division(2, 0))

assert division(4, 2) == 2
assert division(2, 0) == 0