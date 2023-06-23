import math

amount = int(input('введите бюджет'))
price = int(input('введите цену'))
things = (math.floor(amount/price))
print(things)