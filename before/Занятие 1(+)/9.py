number = 451

digit1 = number // 100  # получаем первую цифру числа (1)
digit2 = (number % 100) // 10  # получаем вторую цифру числа (2)
digit3 = number % 10  # получаем третью цифру числа (3)

reversed_number = digit3 * 100 + digit2 * 10 + digit1  # переворачиваем число

print(reversed_number)  # выводим перевернутое число (321)
