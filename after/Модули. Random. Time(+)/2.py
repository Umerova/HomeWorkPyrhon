import random

n1 = int(input("Число участников сборной 1: "))
n2 = int(input("Число участников сборной 2: "))

while True:
    swimmer1 = random.randint(1, n1)
    swimmer2 = random.randint(1, n2)
    print(f"Пловец {swimmer1} - пловец {swimmer2}")
    repeat = input("Нажмите Enter для следующей пары или введите 'stop' для выхода: ")
    if repeat == "stop":
        break
