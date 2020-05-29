"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

path_to_input_file  = './les5_task4_input.txt'
path_to_output_file = './les5_task4_output.txt'

translate_table = {
                   'One':   'Один',
                   'Two':   'Два',
                   'Three': 'Три',
                   'Four':  'Четыре',
                   'Five':  'Пять'
                  }

with open(path_to_input_file, 'r', encoding='UTF-8', errors='ignore') as input_file:
    with open(path_to_output_file, 'w', encoding='UTF-8', errors='ignore') as output_file:
        for input_line in input_file:
            temp = input_line.split('-')
            output_file.write(f'{translate_table.get(temp[0].strip())} - {temp[1].strip()}\n')
        output_file.close()
    input_file.close()

