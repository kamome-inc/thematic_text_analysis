# Реализация Частотного метода выделения ключевых слов текста
# Обрабатывает информацию из файла .txt
import time
import string

start = time.time()


# Переменные и массивы
name_of_file = '1.txt'              # Имя открываемого файла
min_len_of_word = 4                 # Минимальная длинна обрабатываемого слова (для отсечения И, ИЛИ, НО, ЕСЛИ)
number_of_words_in_output = 10      # Число выводимых слов

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
        if mass_valued_words.count(word) != 1:
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
if len(mass_of_appearances) != num_of_word:
    print("Ты ДОЛБОЕБ")

# Сортировка (Ранжирование) массивов по убыванию количества повторов слова
for i in range(num_of_word-1):
    for j in range(num_of_word-i-1):
        if mass_values[j] < mass_values[j+1]:
            mass_values[j], mass_values[j+1] = mass_values[j+1], mass_values[j]
            mass_valued_words[j], mass_valued_words[j + 1] = mass_valued_words[j + 1], mass_valued_words[j]
            mass_of_appearances[j], mass_of_appearances[j+1] = mass_of_appearances[j+1], mass_of_appearances[j]
            # print(mass_valued_words[j + 1], mass_valued_words[j])


# Блок вывода всей тестовой хрени
print('Всего слов в тексте: ', all_words)
print('Уникальных слов в тексте: ', num_of_word)
print('Коэффициент корректности выделения тематики: %.3f' % (num_of_word/all_words))
sum = 0
# Вывод информации по количеству использованний уникальных слов и процентного соотношения их к словам текста
print(' '*12, 'слово', ' '*10, 'Кол-во', ' '*3, '%', ' '*5)
for i in range(num_of_word):
    if i == number_of_words_in_output:
        break
    coeff = mass_values[i]/all_words*100
    print('%-30s' % mass_valued_words[i], ' %-6d' % mass_values[i], '%-10.4f' % coeff, '% ', mass_of_appearances[i])


end = time.time()
print('Время выполнения: %.4f' % (end - start), 'с.')

