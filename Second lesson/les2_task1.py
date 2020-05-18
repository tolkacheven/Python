"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""
random_list = [200, 'String', 222.22, ['Another list', None], 0x111AF, complex(1, 2), False]

for el in random_list:
    print(f'Element type is {type(el)}')
    if type(el) is list:
        print('Element has a list type:')
        for el_inside_list in el:
            print(f'   > Subelement type is {type(el_inside_list)}')