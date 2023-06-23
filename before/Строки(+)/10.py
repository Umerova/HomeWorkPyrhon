phone_number = input("Введите номер телефона: ")
formatted_phone_number = phone_number.replace("+", "").replace("(", "").replace(")", "") #replace удаляет
print("Форматированный номер телефона: ", formatted_phone_number)
