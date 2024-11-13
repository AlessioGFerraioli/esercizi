'''

2024.10.31 17.23
esercizio palindromo


scrivete un programma
che utilziza una funzione che accetta come parametro
una stringa passata dall'utente
e resitutisce in risposta 
se è palindorma o no



'''


def clean_string(stringa): 
    '''
    prende input stringa e la pulisce,
    rimuovendo i caratteri non alfabetici 
    e facendo tutto lowercase
    restituisce la stringa pulita
    '''
    stringa_clean = ''
    for c in stringa:
        if c.isalpha():
            stringa_clean = stringa_clean + c
    return stringa_clean.lower()

def mirror_check(stringa):
    '''
    controlla se stringa è uguale al suo reverse
    ritorna True o False
    '''
    stringa_reverse = stringa[::-1]
    print("stringa_reverse")
    print(stringa_reverse)
    if stringa_reverse == stringa:
        return True
    else:
        return False

def check_stringa_palindroma(stringa):
    '''
    controlla se la frase fornita in "stringa" è palindroma
    per contorllare la palindromia ignora i caratteri non alfabetici
    e non è case senstive
    ritorna un True se palindroma, False se no    
    '''
    # rimuovi caratteri non alfabetici e fai tutto lowercase
    stringa_clean = clean_string(stringa)
    # controlla se la stringa pulita al contrario è uguale
    palindroma = mirror_check(stringa_clean)
    return palindroma


# chiedi stringa a utente 
stringa_utente = input("Inserisci una frase: ")
# controlla se sia palindroma
palindroma = check_stringa_palindroma(stringa_utente)
# stampa un messaggio che dice se è palindroma o no
if palindroma == True: 
    print(f"'",stringa_utente,"' è palindroma")
else: 
    print(f"'",stringa_utente,"' non è palindroma")

