"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""
def my_func(x: float, y: int):
    return x**y

def my_func2(x: float, y: int):
    result = 1
    if y == 0:
        return 1
    elif y > 0:
        for i in range(y):
            result *= x
    else:
        for i in range(abs(y)):
            result /= x
    return result

assert my_func(10, 2)   == 100
assert my_func2(10, 2)  == 100
assert my_func(10, -2)  == 0.01
assert my_func2(10, -2) == 0.01