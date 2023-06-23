grades = []  # Список оценок

while True:
    grade = input("Введите оценку (или 0 для завершения): ")

    if grade == "0":
        break

    if grade not in ["2", "3", "4", "5"]:
        print("Неверная оценка. Введите оценку от 2 до 5.")
        continue

    grades.append(grade)

total_grades = len(grades)
grade_counts = {grade: grades.count(grade) for grade in ["2", "3", "4", "5"]}

print("Список оценок:", grades)
print("Количество оценок:")
for grade, count in grade_counts.items():
    print(grade + ":", count)

performance = (grades.count("5") + grades.count("4") + grades.count("3")) / total_grades * 100
print("Успеваемость: {:.2f}%".format(performance))
