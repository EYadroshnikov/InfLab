# доп. Ввести строку и индекс(число), вывести слова по алфавиту (индекс определяет по какой букве сортировать)
# Пример: asfcvb fsdfds 32zz xcvcb -  индекс = 3, сортировать по 3-ей букве
#  eng   |  rus
# A - 65 | А - 1040
# a - 97 | а - 1072
# diff - 32

# функция приводит первый символ к нижнему регистру если первая буква не находится в диапазоне символов нижнего
# регистра (97 - 122 или 1072 - 1103), то функция возвращает строку, состоящую из первого символа + сдвиг до нижнего
# регистра и исходное слово без первого символа
def lower(word, idx):
    if not ('a' <= word[idx] <= 'z' or 'а' <= word[idx] <= 'я'):
        return word[:idx] + chr(ord(word[idx]) + 32) + word[idx + 1:]
    return word


words = input().split()
index = int(input()) - 1

# Сортировка пузырьком, но сравниваются временные переменные t_wordi и t_wordj.
# В них содержатся слова всегда с нижним регистром.
# Это сделано для правильного сравнения с сохранением исходных слов.
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        t_wordi = lower(words[i], index)
        t_wordj = lower(words[j], index)

        if t_wordi[index] > t_wordj[index]:
            words[i], words[j] = words[j], words[i]

print(' '.join(words))
