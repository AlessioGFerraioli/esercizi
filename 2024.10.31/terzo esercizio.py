'''

2024.10.31 15.37

terzo esercizio

Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10

'''



def inserisci_alunno(dizionario_alunni):
    nome = input("Digita il nome dell'alunno da inserire: ")
    # controllare sia già inserito
    if nome in dizionario_alunni:
        print("Alunno già presente. ")
    else:
        dizionario_alunni[nome] = []
        print(f"Alunno ",nome,"registrato. ")
        print()
    return dizionario_alunni

def inserisci_voto(dizionario_alunni):
    nome = input("Digita il nome dell'alunno a cui inserire il voto: ")
    # controllare se esiste
    if nome in dizionario_alunni:
        voto = int(input("Digita il voto da assegnare all'alunno "))
        dizionario_alunni[nome].append(voto)
        print("Voto aggiunto.")
        print()
    else:
        print("Nessun alunno con questo nome. ")
    return dizionario_alunni

def average(lista):
    return sum(lista)/len(lista)

def mostra_media(dizionario_alunni):
    for nome in dizionario_alunni:
        media = average(dizionario_alunni[nome])
        print(f"Nome: ", nome, "Media: ", media)



# inizializzo dizionario
alunni = {}
continuare = True
while continuare == True:
    risposta = input("Digita a per inserire alunno, v per inserire voto, m per mostrare la media dei voti, q per uscire. ")
    if risposta == "a":
        alunni = inserisci_alunno(alunni)
    elif risposta == 'v':
        alunni = inserisci_voto(alunni)
    elif risposta == 'm':
        mostra_media(alunni)
    elif risposta == 'q':
        continuare = False


