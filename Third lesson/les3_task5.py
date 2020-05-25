"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен
после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
программу.
"""

exit_key = 'q'

# Решение из разбора
def add_more(*args):
    result = 0
    exit_flag = False
    for digit in args:
        try:
            result += float(digit) if digit else 0  # Если digit - не число, добавляем ноль
        except ValueError as error:                 # Проверяем, введен ли символ окончания ввода
            if digit == exit_key:
                exit_flag = not exit_flag           # Меняем значение флага на true
    return result, exit_flag


current_sum = 0
total_sum = 0

while True:
    user_input = input('Введите числа через пробел: ').split(' ')
    current_sum, end_input_flag = add_more(*user_input)
    total_sum += current_sum
    print(f'Текущая сумма: {total_sum}')

    if end_input_flag:
        print('Ввод закончен!')
        break
