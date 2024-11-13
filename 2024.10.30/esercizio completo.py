'''
2024.10.30

Descrizione: Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. 
Il programma deve poi eseguire le seguenti operazioni:

1 Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. 
Se l'utente inserisce un numero negativo o zero, 
il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo.

2 Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.

3 Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.

4 Utilizzare una struttura if per determinare se n è un numero primo.
 Un numero primo è divisibile solo per 1 e per se stesso. 
 Il programma deve stampare se n è primo o no.

'''

richiedere_numero = True
while richiedere_numero == True:
    numero_utente = int(input("Inserisci un numero intero positivo n: "))
    if not (numero_utente > 0):
        print("il numero inserito è negativo.")
    else:
        richiedere_numero = False
    

# 2 Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
# 3 Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
somma_pari = 0
numeri_dispari = []
for numero in range(numero_utente):
    if numero%2 == 0:
        somma_pari += numero
    else: 
        numeri_dispari.append(numero)


print(f"Somma dei numeri pari da 1 a ",numero_utente," = ", somma_pari)
print(f"Lista dei numeri dispari da 1 a ", numero_utente," = ", numeri_dispari)


essere_primo = True
# 4 Utilizzare una struttura if per determinare se n è un numero primo.
for divisore in range(1, numero_utente):
    # se la divisione è intera e il divisore non è 1 né n, allora non è primo ed esco il for
    if numero_utente%divisore == 0 and divisore != 1 and divisore != numero_utente:
        essere_primo = False
        print("Il numero non è primo.")
        break

if essere_primo == True:
    print("Il numero è primo")