tracks = {}  # Создаем пустой словарь для хранения информации о треках

while True:
    place = input("Введите место в чарте (или 'off' для выхода): ")
    if place == "off":
        break

    artist = input("Введите имя исполнителя: ")
    title = input("Введите название трека: ")

    tracks[(place, artist)] = title  # Добавляем информацию о треке в словарь

print(tracks)
