grades = input("Введите оценки студента через пробел: ").split()
all_grades = len(grades)
fives_count = grades.count("5")
fives_percentage = (fives_count / all_grades) * 100

print("Число всех оценок:", all_grades)
print("Число пятёрок:", fives_count)
print("Процент пятёрок: {:.2f}%".format(fives_percentage))
