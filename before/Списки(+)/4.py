teachers = []  # Список для хранения информации о наставниках

while True:
    surname = input("Введите фамилию преподавателя (или 0 для завершения): ")

    if surname == "0":
        break

    position = input("Введите должность преподавателя: ")
    groups = list(map(int, input("Введите количество студентов в группах через запятую: ").split(",")))

    teachers.append([surname, position, groups])

print("Информация о наставниках:")
for teacher in teachers:
    print("Фамилия:", teacher[0])
    print("Должность:", teacher[1])
    print("Количество студентов в группах:", teacher[2])
    print()
