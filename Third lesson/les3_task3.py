"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def find_minimum(a: int, b: int, c: int) -> int:
    if a < b:
        return a if a < c else c
    else: return b if b < c else c


def my_func(a: int, b: int, c: int) -> int:
    return (a + b + c) - find_minimum(a, b, c)

def my_func2(a: int, b: int, c: int) -> int:
    return max(a + b, b + c, c + a)


assert my_func(1, 2, 3) == 5
assert my_func2(1, 2, 3) == 5
assert my_func(5, 2, 1) == my_func2(5, 2, 1)