"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""

my_file = open("NewFile.txt", "w+",encoding="UTF-8")
my_file.write("Я гений и стараюсь учить питон")
my_file.seek(0)
n = my_file.read(7)
print(n)
my_file.close()
