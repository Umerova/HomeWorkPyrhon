"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».
Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""
def calculate_discount(points):
    if points >= 100:
        return 0.2
    elif points >= 50:
        return 0.15
    else:
        return 0.1

points = int(input("Введите количество набранных баллов: "))
discount = calculate_discount(points)
print(f"Ваша скидка: Скидка {discount*100}%")