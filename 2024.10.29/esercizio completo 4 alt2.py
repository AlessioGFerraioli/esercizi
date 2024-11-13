'''
esercizio completo 
punto 4 : utilizzo di if while e for insieme


scrivi un sistema che prende in input
una lista di numeri interi
che precedente è stata valorizzata dall'utentea

il sistema deve
1 utilizzare un ciclo for per trovare il numero massimo nella lsita
2 utilzizare un ciclo while per contare quanti numeri sono presenti nella lista
3 utilizzare uan condizione if per stampare "lista vuota" se la lsita è vuota
altrimenti stampare il numero massimo trovato e il numero di elementi nella lista


ALTERNATIVE VERSION: devono inserirsi sia stringhe che numeri
la lunghezza di uans tringa è uil numero di caratteri

'''


# inizializzo lista vuota per i numeri utente
lista_utente = []

continuare_ad_aggiungere = True

# chiedo all'utente di inserire i numeri 
while continuare_ad_aggiungere == True:
    lista_utente.append((input("Inserisci un numero o una parola: ")))
    risposta = input("Vuoi aggiungere altri elementi alla lista? y/n ")
    risposta = risposta.lower()
    if not((risposta == "y") or (risposta == "yes")):
        continuare_ad_aggiungere = False

# stampa la lista
print()
print(f"Lista inserita: ")
print(lista_utente)

valore_max = 0
# 1 utilizzare un ciclo for per trovare il numero massimo nella lsita
for elemento in lista_utente:
    if isinstance(elemento, str):
        valore = len(elemento)
    else:
        valore = elemento
    # controllare se è il massimo
    if valore > valore_max:
        valore_max = valore
        elemento_max = elemento



# 2 utilzizare un ciclo while per contare quanti numeri sono presenti nella lista
lunghezza_lista = 0
i = 0
while i < len(lista_utente):
    lunghezza_lista += 1
    i += 1

# equivalente a len(lunghezza_lista)
# altrimenti si potrebbe fare con un try except



# 3 utilizzare uan condizione if per stampare "lista vuota" se la lsita è vuota
if lunghezza_lista == 0:
    print("lista vuota")
else: 
    #altrimenti stampare il numero massimo trovato e il numero di elementi nella lista
    print(f"Numero o stringa massima nella lista: ", elemento_max)
    print(f"Lunghezza lista: ",lunghezza_lista)
