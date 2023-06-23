games_list = []  # Список игр

while True:
    game = input("Введите название настольной игры (или 0 для завершения): ")

    if game == "0":
        break

    if game in games_list:
        print("Эта игра уже записана.")
    else:
        games_list.append(game)
        games_list.sort()  # Сортировка списка

print("Список настольных игр:")
for game in games_list:
    print(game)
