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


for word in mass_words:
    if len(word) > 4:
        if mass_valued_words.count(word) != 1:
            mass_valued_words.append(word)
            mass_values.append(1)
        else:
            i = mass_valued_words.index(word)
            mass_values[i] += 1

num_of_word = len(mass_values)
all_words = len(mass_words)
for i in range(num_of_word-1):
    for j in range(num_of_word-i-1):
        if mass_values[j] < mass_values[j+1]:
            mass_values[j], mass_values[j+1] = mass_values[j+1], mass_values[j]
            mass_valued_words[j], mass_valued_words[j + 1] = mass_valued_words[j + 1], mass_valued_words[j]
            # print(mass_valued_words[j + 1], mass_valued_words[j])

# Блок вывода всей тестовой хрени
print('Уникальных слов в тексте: ', num_of_word)
sum = 0
for i in range(num_of_word):
    coeff = mass_values[i]/all_words*100
    sum += coeff
    print(mass_valued_words[i], ' ', mass_values[i], ' ', coeff, '%')

print(sum)