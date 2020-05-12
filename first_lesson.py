# Задание 1:  Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько
#             чисел и строк и сохраните в переменные, выведите на экран.
task1_fst_var = input('Введите первую переменную: ')
task1_scd_var = input('Введите вторую переменную: ')
if task1_fst_var.isdigit:
    task1_fst_var = int(task1_fst_var)
    task1_fst_var **= 2
    print('Первая переменная является числом. Возводим в квадрат:', task1_fst_var)
    if task1_scd_var.isdigit:
        task1_scd_var = int(task1_scd_var)
        task1_trd_var = task1_fst_var % task1_scd_var
        task1_fourth_var = task1_trd_var
        print('Остаток:', task1_trd_var)
        if task1_fourth_var is task1_trd_var:
            print('Переменные указывают на один объект:', task1_fourth_var)
            task1_trd_var -= 1
            if task1_fourth_var is task1_trd_var:
                print('Значения по-прежнему равны => они хранят указатель на один объект:\n\n', task1_fourth_var)
            else:
                print('После изменения переменные указывают на разные объекты: {0:d} и {1:d}\n\n'.format(task1_trd_var, task1_fourth_var))

else:
    print('Первая переменная указывает на объект строкового типа\n')




# Задание 2: Пользователь вводит время в секундах. Перевести время в часы, минуты и секунды и вывести в формате чч:мм:сс
input_seconds  = input('Задание 2. Введите количество секунд для перевода: ')
output_hours   = 0
output_minutes = 0
output_seconds = 0
if input_seconds.isdigit:
    input_seconds  = int(input_seconds)
    output_hours   = input_seconds // 3600
    input_seconds -= output_hours   * 3600
    output_minutes = input_seconds // 60
    input_seconds -= output_minutes * 60
    output_seconds = input_seconds
    print('{0:02d}:{1:02d}:{2:02d}\n\n'.format(output_hours, output_minutes, output_seconds))




# Задание 3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn (предполагаю, что |n| < 10)
# Или я не правильно понял задачу, и нужно конкатенацией строк формировать числа n, nn и nnn, после чего
# приводить к числовому типу?
task3_n_value = input('Задание 3. Сумма n, nn и nnn. Введите значение n: ')
if task3_n_value.isdigit:
    task3_n_value = int(task3_n_value)
    if abs(task3_n_value) < 10:
        print(task3_n_value + (11 * task3_n_value) + (111 * task3_n_value), "\n\n")
    else:
        print('Введено некорректное значение! (|n| < 10)\n')




# Задание 4: Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#            Для решения используйте цикл while и арифметические операции.

task4_some_digit = input('Задание 4. Поиск наибольшей цифры в числе. Введите число: ')
if task4_some_digit.isdigit:
    task4_some_digit = int(task4_some_digit)
    current_max = -1                                # Переменная, хранящая максимальное значение
    while task4_some_digit:
        current_digit = task4_some_digit % 10       # Текущая цифра в числе (получаем как остаток от деления)
        if current_digit >= current_max:            # Если полученная цифра больше текущего максимума - обновляем
            current_max = current_digit
        task4_some_digit //= 10                     # Делим нацело на 10, чтобы отбросить последнюю цифу
    print('Максимальная цифра в числе: {0:d}\n\n'.format(current_max))




# Задание 5: Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
#            результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#            Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
#            (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы
#            в расчете на одного сотрудника.

income = input('Задание 5. Введите значение выручки: ')
expenses = input('Введите значение издержек: ')

if income.isdigit and expenses.isdigit:
    income = float(income)
    expenses = float(expenses)

if income > expenses:
    print('Прибыль. Рентабельность:', (income - expenses) / income)
    number_of_staff = input('Введите количество сотрудников: ')
    if number_of_staff.isdigit:
        number_of_staff = int(number_of_staff)
        print('Прибыль фирмы в расчете на одного сотрудника:', (income - expenses) / number_of_staff, '\n')
else:
    print('Убыток\n')



# Задание 6: Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
#            Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер
#            дня, на который общий результат спортсмена составить не менее b километров.
#            Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
sportsmen_result = input('Введите результат спортсмена за первый день: ')
sportsmen_target = input('Сколько должен составлять конечный результат спортсмена: ')
if sportsmen_result.isdigit and sportsmen_target:
    count_of_days = 1                               # Отсчет с 1, т.к. мы потратили день для замера первого результата
    sportsmen_result = float(sportsmen_result)
    sportsmen_target = float(sportsmen_target)
    while sportsmen_result < sportsmen_target:
        sportsmen_result *= 1.1
        count_of_days += 1
    print(count_of_days)

