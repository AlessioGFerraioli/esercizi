'''
2024.10.30 14:34

chiedere 3 input all'utente: bool, intero, stringa
salvarli in un dict con chiave 'tipo_del_dato'

'''

dizionario = {
    "bool" : None,
    "intero" : None,
    "stringa" : None,
}

dizionario["bool"] = input("Inserisci un booleano (True/False): ")
dizionario["intero"] = input("Inserisci un numero intero: ")
dizionario["stringa"] = input("Inserisci una stringa: ")

print(dizionario)