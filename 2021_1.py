# Реализация Частотного метода выделения ключевых слов текста
# Обрабатывает информацию из файла .txt
import time
import string
import math

start = time.time()


# Переменные и массивы
#name_of_file = '1.txt'              # Имя открываемого файла
min_len_of_word = 4                 # Минимальная длинна обрабатываемого слова (для отсечения И, ИЛИ, НО, ЕСЛИ)
r = 2                               # Радиус поиска окресности


def texting(name_of_file):
    mass_words = []  # Массив всех слов из файла
    mass_valued_words = []  # Массив уникальных слов
    mass_values = []  # Массив количества повторений

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

    #for i in range(num_of_word-1):
        #print(mass_valued_words[i], "   ", mass_values[i])

    print(len(mass_words))
    return mass_valued_words[:10000], mass_values[:10000], len(mass_words)


D = [r'temo\2 — копия (1).txt', r'temo\2 — копия (2).txt', r'temo\2 — копия (3).txt', r'temo\2 — копия (4).txt',
     r'temo\2 — копия (5).txt', r'temo\2 — копия (6).txt', r'temo\2 — копия (7).txt', r'temo\2 — копия (8).txt',
     r'temo\2 — копия (9).txt', r'temo\2 — копия (10).txt']

MMM_words = []
MMM_values = []
MMM_len_text = []
MMM_new_values = []
for d in D:
    print(d)
    m_words1, m_values1, len_text1 = texting(d)
    MMM_words.append(m_words1)
    MMM_values.append(m_values1)
    MMM_len_text.append(len_text1)


def find_a_docs(word):
    k = 0
    for text in MMM_words:
        try:
            if text.index(word):
                k += 1
        except:
            k += 0
    return k


for j in range(len(MMM_words)):
    Words = MMM_words[j]
    Values = MMM_values[j]
    Len_text = MMM_len_text[j]
    New_values = []
    for i in range(len(MMM_words[j])):
        TF = Values[i]/Len_text
        try:
            IDF = math.log10(len(D)/find_a_docs(Words[i]))
        except:
            IDF = 1
        New_values.append(TF*IDF)
    MMM_new_values.append(New_values)


def two_text_analize(id_doc1, id_doc2):
    m_words1 = MMM_words[id_doc1]
    m_new_values2 = MMM_new_values[id_doc2]
    m_words2 = MMM_words[id_doc2]
    m_new_values1 = MMM_new_values[id_doc1]
    p = 0
    for i in range(len(m_words1)):
        try:
            try:
                s = m_new_values2[m_words2.index(m_words1[i])]
            except ValueError:
                s = 0
            if m_new_values1[i] >= s:
                p = p + ((s / m_new_values1[i]) * m_new_values1[i])
            else:
                p = p + ((m_new_values1[i] / s) * m_new_values1[i])
        except ZeroDivisionError:
            p += 0
    return p


print('n', '\t', 1, '\t', 2, '\t', 3, '\t', 4, '\t', 5, '\t', 6, '\t', 7, '\t', 8, '\t', 9, '\t', 10)
for n in range(len(D)):
    s = str(n+1) + '\t'
    for m in range(len(D)):
        pid = two_text_analize(n, m)
        s = s + '%.4f' % pid + '\t'
    print(s)