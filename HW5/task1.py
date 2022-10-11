# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import re
words = 'Напишите программу, удаляющую из текста все слова, содержащие абв'
word = re.split('\W+', words)
delete = ['а', 'б', 'в']
for i in range(len(word)):
    if word[i].find(delete[0]) != -1 and word[i].find(delete[1]) != -1 and word[i].find(delete[2]) != -1:
         word[i]=None
word=[t for t in word if t]
print(*word) 





