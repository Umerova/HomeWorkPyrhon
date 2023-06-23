numbers = "0139412831055230677798"

digit_count = {}  # Создаем словарь

for digit in numbers:
    if digit.isdigit():
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

print(digit_count)
