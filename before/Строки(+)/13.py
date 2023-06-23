text = input("Введите текст: ")
at_index = text.find("@")
if at_index == -1:
    print("Адрес электронной почты не найден")
    exit()
# Ищем символ . справа от символа @
dot_index = text.rfind(".", at_index)
if dot_index == -1:
    print("Адрес электронной почты некорректный")
    exit()
# Создаем срез из строки, содержащий адрес электронной почты
email = text[at_index+1:dot_index]
print("Адрес электронной почты: ", email)
