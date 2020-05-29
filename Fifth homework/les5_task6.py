"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import os

path_to_file = './les5_task6.txt'
result = {}

with open(path_to_file, 'r', encoding='cp1251') as file:
    for discipline in file.readlines():
        total_hours = 0
        for discipline_hours in discipline.split(':')[1].split(' - '):
            discipline_hours = discipline_hours.strip()
            each_hour = discipline_hours.split('(')
            if each_hour[0].isdigit():
                total_hours += int(each_hour[0])
            else:
                continue

        result[discipline.split(':')[0]] = total_hours

file.close()
print(result)