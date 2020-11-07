###################################################################################
#                             Лабораторная работа № 1                             #
###################################################################################
# Дисциплина: Проектирование, архитектура и конструирование программных средств   #
# Студент: Толкачев Е.Н.                                                          #
# Группа: ИВТ-416                                                                 #
# Вариант 8                                                                       #
###################################################################################
#                                     Задание                                     #
###################################################################################
# 1. Создать класс с полями, указанными в индивидуальном задании.
# 2. Реализовать в классе методы:
#    ✔ Конструктор по умолчанию;
#    ✔ Деструктор для освобождения памяти (с сообщением об уничтожении  объекта);
#    ✔ Функции обработки данных, указанные в индивидуальном задании;
#    ✔ Функцию формирования строки информации об объекте.
# 3. Создать проект для демонстрации работы: сформировать объекты со  значениями-константами и с введенными
#    с клавиатуры значениями полей объекта.  В основной ветке программы создайте три объекта класса. Вывести результаты
#    работы на экран.
#
# Класс-родитель и его поля: Работник - фамилия, оклад, дата рождения;
# Функция-метод 1: Вычислить возраст работника;
# Функция-метод 2: Сколько календарных дней до исполнения работнику 50 лет.
###################################################################################
from datetime import date, datetime

class Employee:
    # Конструктор
    #   1-й аргумент: фамилия -> str;
    #   2-й аргумент: оклад   -> float;
    #   3-й аргумент: дата рождения в формате dd.mm.yyyy -> str, конвертируется в тип datetime.
    def __init__(self, surname: str, salary: float, birthday: str):
        self.surname = surname
        self.salary = salary
        if (len(birthday.split('.')) == 3):
            self.birthday = date(int(birthday.split('.')[2]), int(birthday.split('.')[1]), int(birthday.split('.')[0]))
        else:
            print('> Ошибка: некорректная дата рождения')


    # Вычисление возраста сотрудника
    def age(self) -> int:
        todays_date = datetime.today()
        employee_age = todays_date.year - self.birthday.year
        if ((todays_date.month < self.birthday.month) or ((todays_date.month == self.birthday.month) and (todays_date.day > self.birthday.day))):
            employee_age -= 1
        return employee_age


    # Вычисления количества дней до 50 лет
    def days_to_50(self) -> int:
        if(self.age() >= 50):
            print('Сотруднику 50 лет и более...')
            return 0
        else:
            years_to_50 = 50 - self.age()
            needed_date = datetime(datetime.today().year + years_to_50, self.birthday.month, self.birthday.day)
            result_days = (needed_date - datetime.now()).days
        return result_days



    # Вывод информации о работнике
    def info(self):
        print(f"{self.surname} ({self.birthday}) - оклад: {self.salary}")


    # Деструктор
    def __del__(self):
        print(f"Объект {self.surname} уничтожен")


#####################################################


employees = []

employees.append(Employee('Иванов',  15000, '17.10.1990'))
employees[0].info()
employees[0].age()
print(f'Дней до 50: {employees[0].days_to_50()}')

employees.append(Employee('Петров',  25000, '15.09.1971'))
employees[1].age()

employees.append(Employee('Сидоров', 17000, '22.11.1993'))
employees[2].age()

user_choice = ''
while user_choice != 'q':
    print('\n#   Создание нового сотрудника   #')
    user_input_surname = input('Введите фамилию сотрудника -> ')
    if not user_input_surname:
        print('Некорректное имя!')
        continue

    user_input_date_of_birth = input('Дата рождения (в формате дд.мм.гггг) -> ')
    if not user_input_date_of_birth:
        print('Некорректная дата рождения!')
        continue

    user_input_salary = float(input('Введите оклад сотрудника -> '))

    if user_input_salary.is_integer():
       employees.append(Employee(user_input_surname, user_input_salary, user_input_date_of_birth))
    else:
        print('Некорректный оклад. Введите число!')
        continue

    print(f"Сотрудник {employees[len(employees) - 1].surname} создан. "
          f"Дата рождения: {employees[len(employees) - 1].birthday}, "
          f"оклад: {employees[len(employees) - 1].salary}")
    user_choice = input("\nДля продолжения ввода нажмите Enter, для завершения - q -> ")