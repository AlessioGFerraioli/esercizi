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


'''


# inizializzo lista vuota per i numeri utente
lista_utente = []

continuare_ad_aggiungere = True

# chiedo all'utente di inserire i numeri 
while continuare_ad_aggiungere == True:
    lista_utente.append(float(input("Inserisci un numero: ")))
    risposta = input("Vuoi aggiungere altri numeri alla lista? y/n ")
    risposta = risposta.lower()
    if not((risposta == "y") or (risposta == "yes")):
        continuare_ad_aggiungere = False

# stampa la lista
print(f"Lista numeri inseriti: ")
print(lista_utente)

numero_max = 0
# 1 utilizzare un ciclo for per trovare il numero massimo nella lsita
for numero in lista_utente:
    if numero > numero_max:
        numero_max = numero



# 2 utilzizare un ciclo while per contare quanti numeri sono presenti nella lista
lunghezza_lista = len(lista_utente)

# 3 utilizzare uan condizione if per stampare "lista vuota" se la lsita è vuota
if lunghezza_lista == 0:
    print("lista vuota")
else: 
    #altrimenti stampare il numero massimo trovato e il numero di elementi nella lista
    print(f"Numero massimo nella lista: ", numero_max)
    print(f"Lunghezza lista: ",lunghezza_lista)
