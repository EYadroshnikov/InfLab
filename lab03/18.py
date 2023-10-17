# 18.  Ввести строку, вывести слова по алфавиту (по первой букве).
#  eng   |  rus
# A - 65 | А - 1040
# a - 97 | а - 1072
# diff - 32

def lower(word):
    if not ('a' <= word[0] <= 'z' or 'а' <= word[0] <= 'я'):
        return chr(ord(word[0]) + 32) + word[1:]
    return word


words = input().split()

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        t_wordi = lower(words[i])
        t_wordj = lower(words[j])

        if t_wordi[0] > t_wordj[0]:
            words[i], words[j] = words[j], words[i]

print(' '.join(words))
