'''
2024.10.31 14.58


primo esercizio
scrivete un programma che chiede una stringa all'utente e restituisce un dizionario
rappresentatne la freuqneza di comparsa di ciascun carattere
componente la stringa

'''


stringa_input = input("Digita una stringa alfanumerica: ")
if stringa_input.isalpha() == False:
    print("La stringa inserita non è alfanumerica. ")
else:


    # creo un set delle lettere presenti nella stringa
    #stringa_set = {i for i in stringa_input}

    # inizializzo dizionario per contare le occorrenze
    count = {}
    # ciclo per contare quante occorrenze ha ogni lettera diversa (prendendole dal set)
    for lettera in stringa_input:
        count[lettera] = 0
        for elemento in stringa_input:
            if elemento == lettera:
                count[lettera] = count[lettera] + 1

    print()
    print("Conteggio occorrenze lettere nella stringa: ")
    print(count)