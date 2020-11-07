###################################################################################
#                             Лабораторная работа № 3                             #
###################################################################################
# Дисциплина: Проектирование, архитектура и конструирование программных средств   #
# Студент: Толкачев Е.Н.                                                          #
# Группа: ИВТ-416                                                                 #
# Вариант 8                                                                       #
###################################################################################
#                                     Задание                                     #
###################################################################################
# 1. Представьте таблицы (согласно вашему варианту) в виде структур языка Python;
# 2. Реализуйте в консоли интерфейс по добавлению, удалению, изменению
#    данных. Имейте в виду, что связанные операции (удаление, добавление, изменение)
#    для связанных таблиц, должны изменять данных во всех связанных структурах;
# 3. Реализуйте функционал по сохранению данных в файлы формата .csv и считыванию
#    информации из файлов.
#
# Сущности:
#   День недели: ID, Название;
#   Дисциплина: ID, Название, ID_дня_недели, ID_номера_пары;
#   Пара: ID, № пары, время начала, время конца
#
#   Выведите следующую информацию в консоль построчно:
#   Для каждой дисциплины: «Название дисциплины», в какой день недели ведется, на какой паре.
#
#   Посчитайте и выведите результат:
#   Для каждого дня недели: сколько всего пар предусмотрено в этот день.
#
###################################################################################

####################
#    Дисциплины    #
####################
discipline_ID = 0
disciplines = dict()
####################

####################
#    Дни недели    #
####################
day_of_week_ID = 0
days_of_week = dict()
####################

####################
#       Пары       #
####################
lesson_ID = 0
lessons = dict()
####################

class Discipline:
    def __init__(self, name, day_ID, lesson_ID):
        global discipline_ID, disciplines, days_of_week, lessons
        discipline_ID += 1
        self.ID = discipline_ID
        self.info = []
        self.info.append(name)
        self.info.append(days_of_week.get(day_ID))
        self.info.append(lessons.get(lesson_ID))
        disciplines.update({self.ID: self.info})


class DayOfWeek:
    def __init__(self, name):
        global day_of_week_ID
        day_of_week_ID += 1
        self.ID = day_of_week_ID
        self.name = name
        days_of_week.update({self.ID: self.name})


class Lesson:
    def __init__(self, number, start_time, end_time):
        global lesson_ID, lessons
        lesson_ID += 1
        self.ID = lesson_ID
        self.info = []
        self.info.append(number)
        self.info.append(start_time)
        self.info.append(end_time)
        lessons.update({self.ID: self.info})


monday    = DayOfWeek('Понедельник')
tuesday   = DayOfWeek('Вторник')
wednesday = DayOfWeek('Среда')
thursday  = DayOfWeek('Четверг')
friday    = DayOfWeek('Пятница')

lesson_1 = Lesson(1, '09:00', '12:10')
lesson_2 = Lesson(2, '12:20', '15:50')

discipline_1 = Discipline('Математика', 2, 1)
discipline_2 = Discipline('Информатика', 1, 1)
discipline_3 = Discipline('Русский язык', 1, 2)
discipline_4 = Discipline('Биология', 3, 2)

# Задание 1 - Вывести построчно информацию о всех дисциплинах
print("####################################\n"
      "####         Дисциплины         ####\n"
      "####################################")
for discipline_id, discipline_info in disciplines.items():
    print(f"{discipline_id} {discipline_info}")

# Задание 2 - Посчитать, в какие дни сколько пар запланировано
print('\n# Задание 2 - посчитать, в какие дни сколько пар запланировано:')
for day, name in days_of_week.items():
    num_of_lessons = 0
    for discipline_id, discipline_info in disciplines.items():
        if (discipline_info[1] == name):
            num_of_lessons += 1
    print(f'  {name}. Пар запланировано: {num_of_lessons}')