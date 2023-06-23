sentence = "Дефисы нужно заменить на тире, но не в словах типа километр-час"
new_sentence = sentence.replace(' - ', ' \u2014 ').replace('- ', '\u2014').replace(' -', '\u2014')
print(new_sentence)
