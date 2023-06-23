def print_range_decorator(func):
    def wrapper(a, b):
        print(f"Данная функция выводит все числа между {a} и {b}")
        func(a, b)
    return wrapper

@print_range_decorator
def print_numbers_divisible_by_three(a, b):
    for num in range(a + 1, b):
        if num % 3 == 0:
            print(num)
