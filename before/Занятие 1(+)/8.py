number = 145

digit1 = number // 100  # получаем первую цифру числа (1)
digit2 = (number % 100) // 10  # получаем вторую цифру числа (3)
digit3 = number % 10  # получаем третью цифру числа (4)

sum_of_digits = digit1 + digit2 + digit3  # складываем все цифры числа

print(sum_of_digits)  # выводим сумму цифр числа (8)
