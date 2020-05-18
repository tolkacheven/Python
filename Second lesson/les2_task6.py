"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

products = []                        # Конечный список товаров
product_id = 1                       # Уникальный номер продукта
current_product = {}                 # Текущий товар (продукт)
product_name = ' '                   # Название товара
product_price = 0                    # Цена товара
product_quantity = 0                 # Количество товара
product_unit = ''                    # Единица измерения товара

                                     # Для анализа товаров
analysis_product_names  = set()      # Названия товаров
analysis_product_prices = set()      # Цены товаров
analysis_product_quantities = set()  # Количество каждого товара
analysis_product_units  = set()      # Единицы измерения товаров
analysis_result_table   = {}         # Конечная таблица

while product_name != '':
    product_name = input('Введите название продукта: ')
    if len(product_name) == 0:
        print("Неправильное имя, повторите ввод!")
        continue

    product_price = input('Введите стоимость продукта: ')
    if product_price.isdigit():
        product_price = int(product_price)
        if product_price < 0:
            print('Ошибка! Цена не может быть отрицательной')
            continue
    else:
        print('Введенное значение не является цифрой. Повторите ввод!')
        continue

    product_quantity = input('Введите количество продуктов: ')
    if product_quantity.isdigit():
        product_quantity = int(product_quantity)
        if product_quantity < 0:
            print('Ошибка! Количество не может быть отрицательным')
            continue
    else:
        print('Введенное значение не является цифрой. Повторите ввод!')
        continue

    product_unit = input('Введите единицу измерения продукта: ')
    if len(product_unit) == 0:
        print("Неправильная единица измерения, повторите ввод!")
        continue

    current_product = {'название':   product_name,
                       'цена':       product_price,
                       'количество': product_quantity,
                       'ед':         product_unit}

    products.append((product_id, current_product))
    product_id += 1

print('Товары:')
print(products)

for product in products:
    analysis_product_names.add(product[1].get('название'))
    analysis_product_prices.add(product[1].get('цена'))
    analysis_product_quantities.add(product[1].get('количество'))
    analysis_product_units.add(product[1].get('ед'))


analysis_result_table = {'название':   analysis_product_names,
                         'цена':       analysis_product_prices,
                         'количество': analysis_product_quantities,
                         'ед':         analysis_product_units}

print("Аналитическая таблица:")
print(analysis_result_table)