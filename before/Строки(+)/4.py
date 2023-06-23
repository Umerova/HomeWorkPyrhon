
numbers_str = input("Введите два числа, разделенных пробелом: ")
a, b = numbers_str.split()
a, b = b, a
print("Числа, поменянные местами:", ' '.join([a, b]))
