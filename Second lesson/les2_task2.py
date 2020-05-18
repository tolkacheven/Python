"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
#some_even_list = [2, 1, 4, 3, 6, 5]         # Список четной длины   (для тестирования)
#some_odd_list  = [2, 1, 4, 3, 6, 5, 7]      # Список нечетной длины (для тестирования)

#list_to_process = some_odd_list             # Указываем список, который необходимо обработать (для тестирования);

list_to_process = []
current_input = ''

print('Заполнения списка. Введите End для окончания ввода.')
while current_input.lower() != 'end':
    current_input = input('Новый элемент списка: ')
    if current_input.isdigit():
        list_to_process.append(int(current_input))
    else:
        if current_input.lower() != 'end':
            print('Введено некорректное значение!')

print(list_to_process)

list_length = len(list_to_process)          # Вычисляем длину списка;

if not list_length:                         # Если список пуст;
    print('Error: list is empty!')

# Понимаю, что некорректно изменять переменную list_length, просто интересно было решить
# без использования дополнительных переменных и обращаясь к индексам с конца списка
while list_length // 2:
    list_to_process[-list_length], list_to_process[-list_length + 1] = list_to_process[-list_length + 1], list_to_process[-list_length]
    list_length -= 2

print(list_to_process)