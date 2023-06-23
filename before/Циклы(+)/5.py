while True:
    price = float(input("Введите стоимость товара (или 0 для завершения): "))
    if price == 0:
        print("Программа завершена.")
        break
    discount = price * 0.1  # 10% скидка
    discounted_price = price - discount
    print("Стоимость с учетом скидки:", discounted_price)
