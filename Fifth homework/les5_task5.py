"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

path_to_file = './les5_task5.txt'
result = 0

with open(path_to_file, 'r', encoding='UTF-8') as file:
    for digit in file.read().split(' '):
        result += int(digit)

print(f'Результат: {result}')