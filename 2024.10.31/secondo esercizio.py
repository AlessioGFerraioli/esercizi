'''
2024.10.31 14.05


secondo esercziio

scrivete un programma che chiede al'lutente una parola e 
restituisce solo le vocali e l'indice della vocale
all'interno della parola

vocali = ["a", "e", "i", "o", "u"]
parola = input("Digita una parola").lower()

vocali_nella_parola, indici = [(lettera, indice) for (lettera, indice) in (parola, range(len(parola))) if (lettera in vocali)]

print(f"Vocali nella parola: ", parola)

print(f"Indici delle vocali nella paroal: ")

for (vocale, indice) in (vocali_nella_parola, indici):
    print(f"vocale: ", vocale)
    print(f"indice: ", indice)
'''





vocali = ["a", "e", "i", "o", "u"]
parola = input("Digita una parola: ").lower()


vocali_nella_parola = []
indici = []
for i in range(len(parola)):
    if parola[i] in vocali:
        vocali_nella_parola.append(parola[i])
        indici.append(i)
 
print()
print(f"Vocali nella parola: ", vocali_nella_parola)
print()
print(f"Indici delle vocali nella paroal: ")

for i in range(len(vocali_nella_parola)):
    print(f"vocale: ", vocali_nella_parola[i])
    print(f"indice: ", indici[i])
    print()