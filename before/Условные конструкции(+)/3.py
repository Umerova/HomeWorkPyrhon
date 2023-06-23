product1 = int(input('введите цену'))
product2 = int(input('введите цену'))
product3 = int(input('введите цену'))
price = (product1+product2+product3)
if product1<product2<product3:
    print('Акция!')
    print(price/2)
elif product1>product2>product3:
    print('Акция!')
    print(price/3)
else:
    print('К оплате:')
    print(price)

