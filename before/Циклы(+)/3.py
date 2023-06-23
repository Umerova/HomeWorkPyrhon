forbidden_chars = '= ? * ^ $ № @ _'
login = input('Введите логин: ')
used_forbidden_chars = []

for char in login: #проходимся по каждому символу
    if char in forbidden_chars:
        used_forbidden_chars.append(char) #строка добавляет символ char в список used_forbidden_chars.

if used_forbidden_chars:
    print('Вы использовали запрещенные символы в логине:', used_forbidden_chars)
