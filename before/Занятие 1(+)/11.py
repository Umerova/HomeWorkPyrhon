
mass = float(input("Введите вашу массу в килограммах: "))
height = float(input("Введите ваш рост в метрах: "))
bmi = mass / (height ** 2)
print("Ваш ИМТ равен", round(bmi, 1))
