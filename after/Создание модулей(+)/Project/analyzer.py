def router(user_input):
    if "расписание" in user_input.lower():
        print(get_schedule())
    elif "препод" in user_input.lower():
        name = input("Введите имя преподавателя: ")
        print(get_teacher_info(name))
    elif "плат" in user_input.lower():
        print(get_payment())
    elif "транс" in user_input.lower():
        print(get_transfer_days())
    elif "консульт" in user_input.lower():
        print(get_consultations())
    else:
        print("Извините, я не понимаю вас.")

def get_schedule():
    return "1. ОБЖ\n2. История\n3. Физика\n4. Русский язык\n5. Литература"

def get_teacher_info(name):
    if "румянцев" in name.lower():
        return "Подключается по SSH"
    elif "Борис Игоревич".lower() in name.lower():
        return "Подождите. Он составляет новую самостоятельную"

def get_payment():
    return "Бесценно"

def get_transfer_days():
    return "По средам и пятницам"

def get_consultations():
    return "По средам и пятницам"
