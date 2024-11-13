'''
sviluppa una funzione chiamata comprimi_stringa
che prenda in ionput una stringa
e restituisca una versione compressa di essa

la compressione funona in questo modo:
per ogni gruppo consecutivo di caratteri
identici nella stringa, la funzione dovrebba ggiunger eil carattere
seguito dal numero di volte che appare consecutivamente.

per esempio la stringa aaabbc dovrebbe diventare a3b2c1..

se la compressione non riduce la lungheza della stringa, 
la funzione dovrebbe semplicemnete
resitturei la stringa originale


'''


def print_result(function):
    def wrapper(*args, **kwargs)
        result = function(*args, **kwargs)
        print(result)
        return result 
    return wrapper

@print_result
def comprimi_stringa(stringa):
    stringa_compressa = ''
    
    lunghezza_stringa = len(stringa)
    # i lo uso per muovermi sulle lettere della stringa
    i=0
    while i < (lunghezza_stringa):
        # inn questo conterò quante volte si ripete uguale il carattere
        count_ripetizioni = 0
        # j lo uso per muovermi dalla lettera in esame (quella indicata con i) alle seguenti
        j = i
        while (stringa[j] == stringa[i]):
            count_ripetizioni += 1
            j += 1
            # se arrivo alla fine della stringa devo uscire dal ciclo
            if j == lunghezza_stringa:
                break
        # salvo la lettera e il count delle ripetizioni nella stringa_compressa
        stringa_compressa = stringa_compressa + stringa[i] + str(count_ripetizioni)
        # avanzo alla prossima lettera diversa
        i = i + count_ripetizioni

        
    return stringa_compressa


# controllo se la stringa compressa è più corta della stringa non compressa
    #altrimenti rimando indietro la stringa originale
if not(len(stringa_compressa) < len(stringa_input)):
    stringa_compressa = stringa

stringa_input = str(input("Inserisci una stringa: "))
stringa_compressa = comprimi_stringa(stringa_input)

if not(len(stringa_compressa) < len(stringa_input)):
    stringa_compressa = stringa_input

print(f"stringa compressa: ", stringa_compressa)