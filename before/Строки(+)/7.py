fio = input('Введите ФИО: ')
parts = fio.split()  # Разбиваем строку на список подстрок
surname = parts[0]  # Фамилия - это первый элемент списка
initials = '.'.join([name[0] for name in parts[1:]])  # Инициалы - это первые буквы остальных элементов списка
print(f"{surname}. {initials}")

