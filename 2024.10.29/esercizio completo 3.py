'''
esercizio completo 
punto 3 utilizzo di for

scrivi un sistema che prende in input una lsita di numeri
e stampa il quadrato di ciascun numero
nella lista



'''



lunghezza_lista = 4


lista_utente = []



# chiedo all'utente di inserire i numeri 
for i in range(lunghezza_lista):
    lista_utente.append(float(input("Inserisci un numero: ")))
    print(f"Rimangono da aggiungere ", lunghezza_lista-1-i, " numeri. ")

print(f"Lista numeri: ")
print(lista_utente)

#calcoo i quadrati salvandoli in una nuova lista
lista_quadrati = []
for numero in lista_utente:
    lista_quadrati.append(numero**2)
print(f"Lista numeri al quadrato: ")
print(lista_quadrati)
    