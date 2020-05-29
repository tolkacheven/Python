"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
path_to_file = './les5_task3.txt'
staff = []
salary = []
user_input = ' '

with open(path_to_file, 'w', encoding='UTF-8') as file:
    while True:
        user_input = input('Введите фамилию сотрудника и его зарплату через пробел: ').split(' ')
        if user_input[0] and user_input[1].isdigit():
            staff.append(user_input[0])
            salary.append(int(user_input[1]))
        else:
            break

file.close()

# Вывод всех сотрудников с зарплатой меньше 20000
print('Сотрудники с зарплатой менее 20 тысяч:')
employee_index = 0
for employee_salary in salary:
    if employee_salary < 20000:
        print(staff[employee_index])
    employee_index += 1

# Вывод средней зарплаты сотрудника
print(f'Средняя зарплата: {sum(salary)/len(salary)}')