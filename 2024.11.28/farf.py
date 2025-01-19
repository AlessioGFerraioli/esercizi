def farfallinatore(stringa, classico=True):
    vocali = ["a", "e", "i", "o", "u"]
    if classico == True:    
        prev_voc = False
        for c in stringa:
            if c in vocali:
                prev_voc = True
                if classico == False and prev_voc == True:
                    c = c+"f"+c


risposta = input("Digita 1 per versione classica, 2 versione no dittonghi")
if risposta == "1":
    classico = True
elif risposta == "2": 
    classico = False
    no_dittonghi = True

stringa = input("Parola da farfallinizzare: ")
print(farfallinatore(stringa))

