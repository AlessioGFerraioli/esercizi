'''
2024.10.31 14.58


primo esercizio
scrivete un programma che chiede una stringa all'utente e restituisce un dizionario
rappresentatne la freuqneza di comparsa di ciascun carattere
componente la stringa

'''

def main():
    stringa_input = input("Digita una stringa alfanumerica: ")
    # controlli sull'input
    if len(stringa_input) > 50: # troppo lunga
        print("La stringa inserita è troppo lunga (max 50 caratteri). ")
    elif stringa_input.isalpha() == False:
        caratteri_invalidi = []
        for carattere in stringa_input:
            if carattere.isalpha() == False:
                caratteri_invalidi.append(carattere)
        caratteri_invalidi = set(caratteri_invalidi) 
        print(f"Caratteri non consentiti: {caratteri_invalidi}\nLa stringa inserita può contenere solo lettere. ")
    else:
        case_sensitive = False # di base parti come se non fosse case sensitive
        if (stringa_input.lower() != stringa_input) and (stringa_input.upper() != stringa_input): # se ci sono caratteri sia maiuscoli che minuscoli
            case_choice = input("Vuoi che il conteggio caratteri sia case sensitive? y/n: ") # lascia scegliere all'utente
            if case_choice.lower() == "y" or case_choice.lower() == "yes":
                case_sensitive = True

        # creo un set delle lettere presenti nella stringa
        #stringa_set = {i for i in stringa_input}

        if case_sensitive == False:
            stringa_input = stringa_input.lower()

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

main()