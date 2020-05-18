"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
index = 1
input_string = input("Введите строку: ")
words_in_string = input_string.split(' ')

for word in words_in_string:
    if len(word) > 10:
        print(f'{index}. {word[:10]}')
    else:
        print(f'{index}. {word}')
    index += 1