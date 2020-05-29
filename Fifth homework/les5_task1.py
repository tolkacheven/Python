"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
import os

path_to_file = './les5_task1.txt'       # В дальнейшем буду использовать os.path и .dirname
user_input = ' '

with open(path_to_file, 'w', encoding='UTF-8') as file:
    while user_input:
        user_input = input('Введите строку для записи в файл: ')
        file.write(f'{user_input}\n')

file.close()

