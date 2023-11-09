"""Магазин канцтоварів"""
products_list = [('Папір', 10), ('Олівець', 5), ('Блокнот', 20), ('Клей', 3), ('Ножиці', 30)]

print('Наші товари:')
for item in products_list:
    print(f'{item[0]} - {item[1]}грн.')


def add_func(name, price):
    """Функція яка добавляє кортеж до списку"""
    new_record = (name, price)
    products_list.insert(0, new_record)


while True:
    CHECK = 0
    new_item = input('Введіть ім\'я та ціну. Для розділення використовуйте "-" '
                     '\nЗразок "Пластилін-20"\n>')
    new_item = new_item.split('-')
    if new_item[0] != 'end' and len(new_item) == 2:
        for item in products_list:
            if new_item[0] == item[0]:
                CHECK = 1
                print(f'{new_item[0]} вже є, не можливо додати\n')
        if CHECK != 1:
            add_func(new_item[0], new_item[1])
    else:
        break
    for item in products_list:
        print(f'{item[0]} - {item[1]}грн.')

