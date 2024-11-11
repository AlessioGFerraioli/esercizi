'''
2024.11.11 10.40
Part 1 Scrivete un programma che genera 5 numeri casuali e li salva su un file,
'''

import random

numeri_casuali = random.sample(range(1, 20), 5)
print(numeri_casuali)

numeri_stringa = ''
for numero in numeri_casuali:
        numeri_stringa = numeri_stringa + f"{str(numero)},"

with open('file_esercizio_es_file.txt', "w") as filename:
        filename.write(numeri_stringa)
filename.close()

