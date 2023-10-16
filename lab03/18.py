# 18.  Ввести строку, вывести слова по алфавиту (по первой букве).
#  eng   |  rus
# A - 65 | А - 1040
# a - 97 | а - 1072
# diff - 32


# diff - 32 
words = input().split()

for i in range(len(words)):
    for j in range(i+1, len(words)):
        # t_si = words[i] if 'a' <= words[i][0] <= 'z' or 'а' <= words[i][0] <= 'я' else chr(ord(words[i][0]) + 32) + words[i][1:]
        # t_sj = words[j] if 'a' <= words[j][0] <= 'z' or 'а' <= words[j][0] <= 'я' else chr(ord(words[j][0]) + 32) + words[j][1:]
        if not('a' <= words[i][0] <= 'z' or 'а' <= words[i][0] <= 'я'):
            t_si = chr(ord(words[i][0]) + 32) + words[i][1:]
        else:
            t_si = words[i]

        if not('a' <= words[j][0] <= 'z' or 'а' <= words[j][0] <= 'я'):
            t_sj = chr(ord(words[j][0]) + 32) + words[j][1:]
        else:
            t_sj = words[j]

        if t_si[0] > t_sj[0]:
            words[i], words[j] = words[j], words[i]

print(' '.join(words))