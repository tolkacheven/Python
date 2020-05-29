"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""

import os

path_to_file = './les5_task7.txt'

profitable_firms = []
unprofitable_firms = []

firms_incomes = {}
firms_expenses = {}
firms_num_of_lines = {}


with open(path_to_file, 'r', encoding='cp1251') as file:
    for current_firm in file.readlines():
        current_firm_info = current_firm.split(' ')
        if not firms_incomes.get(current_firm_info[0]):
            firms_incomes[current_firm_info[0]] = int(current_firm_info[2])
            firms_expenses[current_firm_info[0]] = int(current_firm_info[3])
            firms_num_of_lines[current_firm_info[0]] = 1
        else:
            firms_incomes[current_firm_info[0]] += int(current_firm_info[2])
            firms_expenses[current_firm_info[0]] += int(current_firm_info[3])
            firms_num_of_lines[current_firm_info[0]] += 1

print(firms_incomes)

for key in firms_incomes:
    if firms_incomes[key] - firms_expenses[key] > 0:
        profitable_firms.append({key, firms_incomes[key]/firms_num_of_lines[key]})
    else:
        unprofitable_firms.append({key, firms_incomes[key] / firms_num_of_lines[key]})

print(f'Прибыльные компании: {profitable_firms}')
print(f'Убыточные компании: {unprofitable_firms}')