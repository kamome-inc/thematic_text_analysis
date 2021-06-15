# Реализация Частотного метода выделения ключевых слов текста
# Обрабатывает информацию из файла .txt
import time
import string

start = time.time()


# Переменные и массивы
name_of_file = '1.txt'              # Имя открываемого файла
min_len_of_word = 4                 # Минимальная длинна обрабатываемого слова (для отсечения И, ИЛИ, НО, ЕСЛИ)
number_of_words_in_output = 10      # Число выводимых слов
r = 2                               # Радиус поиска окресности

mass_words = []                     # Массив всех слов из файла
mass_valued_words = []              # Массив уникальных слов
mass_values = []                    # Массив количества повторений


file = open(name_of_file, 'r')                           # Открытие файла с текстом
text = file.read()
lines = text.splitlines()

# Разбор текста на слова
for line in lines:
    line = line.translate(str.maketrans('', '', string.punctuation))
    temp1 = line.split(' ')
    for word in temp1:
        mass_words.append(word.lower())

# Выборка уникальных слов и подсчет их количества
e = 0                       # Индексация слов в массиве всех слов
mass_of_appearances = []    # Верхний массив появлений каждого уникального слова в потоке

for word in mass_words:
    if len(word) > min_len_of_word:
        if mass_valued_words.count(word) != 1:      # Проверка на наличие этого слова в массиве слов
            mass_e = [e]
            mass_of_appearances.append(mass_e)
            mass_valued_words.append(word)
            mass_values.append(1)
        else:
            i = mass_valued_words.index(word)
            mass_values[i] += 1
            mass_of_appearances[i].append(e)
    e = e + 1


num_of_word: int = len(mass_values)  # Количество уникальных слов
all_words = len(mass_words)     # Количество всего слов в тексте


# Сортировка (Ранжирование) массивов по убыванию количества повторов слова
for i in range(num_of_word-1):
    for j in range(num_of_word-i-1):
        if mass_values[j] < mass_values[j+1]:
            mass_values[j], mass_values[j+1] = mass_values[j+1], mass_values[j]
            mass_valued_words[j], mass_valued_words[j + 1] = mass_valued_words[j + 1], mass_valued_words[j]
            mass_of_appearances[j], mass_of_appearances[j+1] = mass_of_appearances[j+1], mass_of_appearances[j]
            # print(mass_valued_words[j + 1], mass_valued_words[j])


# Выборка окрестностей
""" Все окрестности для топ num_of_word ключевых слов хранятся в массиве mass_of_surroundings.
    В этом массиве находятся массивы mass_specific_surroundings, каждый из которых содержит массивы с окрестностсями для
    каждого появления конкретного слова specific_surroundings
"""
mass_of_surroundings = []                                # Массив всех окрестностей
for i in range(num_of_word):
    mass_specific_surroundings = []                      # Массив окрестностей для конкретного слова

    if i == number_of_words_in_output:
        break
    for j in range(len(mass_of_appearances[i])):
        specific_surroundings = []                      # Окресности для конкретного появления слов
        appear = mass_of_appearances[i][j]
        # specific_surroundings.append(mass_words[appear-2])
        specific_surroundings.append(mass_words[appear-1])
        specific_surroundings.append(mass_words[appear])
        specific_surroundings.append(mass_words[appear+1])
        # specific_surroundings.append(mass_words[appear+2])
        mass_specific_surroundings.append(specific_surroundings)
    mass_of_surroundings.append(mass_specific_surroundings)

# Обработка окресностей при помощи частотного метода
expression = []         # Массив словосочитаний
weight_exp = []         # Вес словосочитаний
identicalL = 0          # Идентичные слова слева
identicalR = 0          # Идентичные слова справа
numL = 0                # Номер итерации, на которой было обнаружено совпадение слева
numR = 0                # Номер итерации, на которой было обнаружено совпадение справа
num = 0                 # Номер итерации вложенного цикла

for i in range(len(mass_of_surroundings)):              # ОБрабатываем Массивы всех окрестностей для каждого слова
    if identicalL > identicalR:  # определяет какое слово имеет больший вес и вписывает его в массив
        expression.append(mass_of_surroundings[i - 1][numL][0] + ' ' + mass_of_surroundings[i - 1][numL][1])
        weight_exp.append(identicalL)
    elif identicalL < identicalR:
        expression.append(mass_of_surroundings[i - 1][numL][1] + ' ' + mass_of_surroundings[i - 1][numR][2] + ' ')
        weight_exp.append(identicalR)
    elif (identicalL == identicalR) > 1:  # При равенстве веса, отличного от нуля, то словосоч. записывается в массив
        expression.append(mass_of_surroundings[i - 1][numL][0] + ' ' + mass_of_surroundings[i - 1][numR][1] +
                          mass_of_surroundings[i - 1][numR][2])
        weight_exp.append(identicalL)

    identicalL = 0      # Обнуление счетчиков
    identicalR = 0
    numL = 0
    numR = 0
    for j in range(len(mass_of_appearances[i]) - 1):        # обрабатываем массивы конкретной окрестности слова
        if mass_of_surroundings[i][j][0] == mass_of_surroundings[i][j + 1][0]:  # Определяет совпадение слов слева
            identicalL += 1
            numL = j
        if mass_of_surroundings[i][j][2] == mass_of_surroundings[i][j + 1][2]:  # Определяет совпадение слов слева
            identicalR += 1
            numR = j

# Сортировка (Ранжирование) словосочитаний по их весу
for i in range(len(weight_exp)-1):
    for j in range(len(weight_exp)-i-1):
        if weight_exp[j] < weight_exp[j+1]:
            weight_exp[j], weight_exp[j+1] = weight_exp[j+1], weight_exp[j]
            expression[j], expression[j + 1] = expression[j + 1], expression[j]


# Блок вывода всей тестовой хрени
print('Всего слов в тексте: ', all_words)
print('Уникальных слов в тексте: ', num_of_word)
print('Коэффициент корректности выделения тематики: %.3f' % (num_of_word/all_words))

# Вывод информации по количеству использованний уникальных слов и процентного соотношения их к словам текста
print(' '*8, 'слово', ' '*13, 'Словосочетание', ' '*3, 'Вес словосоч.', ' ', 'Вес слов', ' '*2, '%')
f = open('log.txt', 'a')
for i in range(len(expression)):
    if i == number_of_words_in_output:
        break
    coeff = mass_values[i]/all_words*100
    print('%-25s' % mass_valued_words[i], '%-25s' % expression[i], ' ', '%-11s' % weight_exp[i],
          ' %-6d' % mass_values[i], '% 10.4f' % coeff, '% ')
    f.write(mass_valued_words[i] + '->' + str(expression[i]) + '|вес словосочитания ->' + str(weight_exp[i])
            + '|вес слова ->' + str(mass_values[i]) + '|уникальность слова ->' + str(coeff) + '%' + '\n')

f.close()
end = time.time()
print('Время выполнения: %.4f' % (end - start), 'с.')