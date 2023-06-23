category = str(input('введите категорию товара'))
if category == 'продукты':
    price = int(input('Введите цену'))
    if price < 100:
        print('Попробуйте нашу выпечку!')
    elif price >= 100 and price < 500:
        print('Как насчет орехов в шоколаде?')
    elif price >= 500:
        print('Попробуйте экзотические фрукты!')
else:
    print('Попробуйте экзотические фрукты!')

