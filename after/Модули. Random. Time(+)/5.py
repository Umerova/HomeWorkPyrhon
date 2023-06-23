import random
import time

def roll_dice():
    print("Подбрасываем кубики...")
    time.sleep(2) # создаем паузу в 2 секунды
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Значения на кубиках: {dice1} {dice2}")

roll_dice() # вызываем функцию для подбрасывания кубиков
