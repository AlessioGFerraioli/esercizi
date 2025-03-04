''' 
2024.11.05 15.36
esempio di contenimento/incapsulamento


'''



class Computer:
    def __init__(self):
        self.__processore = "Intel i5"  # attributo privato

    def get_processore(self):
        return self.__processore
    
    def set_processore(self, processore):
        self.__processore = processore 

pc = Computer()
print(pc.get_processore())

# Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5")

# Modifica l'attributo privato tramite il setter
print(pc.get_processore())

#print(pc.__processore)  # questa da errore

print(pc._Computer__processore)