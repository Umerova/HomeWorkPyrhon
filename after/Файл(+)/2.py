"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
old_file = open("another_file.txt", "w+",encoding="UTF-8")
old_file.write("но у меня не получается")
old_file.close()

with open('NewFile.txt', 'r') as file1:
    data1 = file1.read()

with open('another_file.txt', 'r') as file2:
    data2 = file2.read()

with open('merged_file.txt', 'w',encoding="UTF-8") as merged_file:
    merged_file.write(data1+", "+data2)
