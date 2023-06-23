my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

keys = list(my_dict.keys())
values = list(my_dict.values())

keys[0], keys[-1] = keys[-1], keys[0]
values[0], values[-1] = values[-1], values[0]

del keys[1]
del values[1]

keys.append("new_key")
values.append("new_value")

my_dict = dict(zip(keys, values))  # Создаем новый словарь из обновленных ключей и значений

print(my_dict)
