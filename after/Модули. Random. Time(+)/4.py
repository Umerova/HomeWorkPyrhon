import time

def disciplinary_penalty():
    remove_from_field = input("Удалить с поля? (да/нет): ")
    if remove_from_field.lower() == "да":
        penalty_time = int(input("Введите количество минут штрафа (2 или 10): "))
        print(f"Вы удалены с поля на {penalty_time} минут(-ы)")
        time.sleep(penalty_time * 60)  # создаем задержку в выполнении на количество минут штрафа
        print("Возвращайтесь на поле!")
    else:
        print("Хорошая игра! До новых встреч.")

disciplinary_penalty() # вызов функции для исполнения кода
