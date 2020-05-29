"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
import os

path_to_file = './les5_task2.txt'

with open(path_to_file, 'r', encoding='UTF-8') as file:
    result = len(file.read().split('\n'))

print(f'Количество строк: {result}')
file.close()