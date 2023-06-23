import sys

if len(sys.argv) < 3:
    print("Usage: python colors.py <Цвета> <количество цветов> <цвет1> <HEX1> <цвет2> <HEX2> ...")
    sys.exit(1)

# Получаем количество цветов из второго аргумента
num_colors = int(sys.argv[2])

# Выводим на экран заголовок
print(sys.argv[1], "({} шт.):".format(num_colors))

# Перебираем все оставшиеся аргументы по парам и выводим их на экран
for i in range(num_colors):
    # Получаем название и значение цвета
    color_name = sys.argv[3 + i * 2]
    color_hex = sys.argv[4 + i * 2]

    # Выводим их на экран в формате "Цвет: HEX"
    print(color_name + ":", color_hex)
