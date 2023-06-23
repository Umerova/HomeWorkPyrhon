entertainment = input('введите развлечение: ')
if entertainment == 'game':
    secret_number = 5
    attempts = 3
    for i in range(attempts):
        guess = int(input("Угадайте число от 1 до 10: "))
        if guess == secret_number:
            print("Вы выиграли билет на концерт!")
            break
        elif i < attempts - 1:
            print("Неправильно. Попробуйте еще раз.")
    else:
        print("Вы исчерпали все попытки. Было загадано число", secret_number)
else:
    print('других развлечений нет')



