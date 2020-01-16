# Реализация Частотного метода выделения ключевых слов текста

# Обрабатывает информацию из файла .txt
mass_words = []             # Массив всех слов из файла
mass_valued_words = []      # Массив уникальных слов
mass_values = []            # Массив количества повторений


file = open("1.txt", 'r')
text = file.read()
lines = text.splitlines()
for line in lines:
    temp1 = line.split(' ')
    for word in temp1:
        mass_words.append(word.lower())
num_of_word = len(mass_words)

for word in mass_words:
    if mass_valued_words.count(word) != 1:
        mass_valued_words.append(word)
        mass_values.append(1)
    else:
        i = mass_valued_words.index(word)
        mass_values[i] += 1

# Блок вывода всей тестовой хрени
print(num_of_word)
print(mass_words)
print(mass_valued_words)
print(mass_values)