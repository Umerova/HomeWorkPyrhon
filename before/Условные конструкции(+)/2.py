summ = int(input('введите сумму покупки'))
time = str(input('введите время'))
if time >= "10:00" and time <= "12:00":
    print(summ/2)
elif time >= "20:00" and time <= "22:00":
    print(summ/4)
else:
    print(summ)