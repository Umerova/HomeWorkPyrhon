import random

run1 = 0
run2 = 0

while True:
    num = input("Введите любой символ для генерации номера забега или 'off' для выхода: ")
    if num == "off":
        break
    race = random.randint(1, 2)
    if race == 1:
        run1 += 1
    else:
        run2 += 1
    print(f"Ваш номер: {race}")
    print(f"Участников в первом забеге: {run1}")
    print(f"Участников во втором забеге: {run2}")
