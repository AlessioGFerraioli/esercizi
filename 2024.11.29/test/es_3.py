'''
Crea un dataset autogenerandolo monolineare con 50 numeri random 
e cambia la sua forma in 10 file da 5, 
normalizza i valori e rendili interi ,
 nessun valore deve essere uguale a un altro sulla stessa linea della collezione
  dopodiché stampa un grafico che lo rappresenti. 
'''

import numpy as np
import matplotlib.pyplot as plt

# Crea un dataset monolineare

np.random.seed(666)
size = 50
numeri = []
n_iter = 0

while len(numeri) < size and n_iter < 100:
    # genero cinque dati alla volta per assicurarmi che siano tutti diversi in gruppi da ccinque
    riga = np.random.randint(1, 100, size=(5,))
    print(f"Riga prodotta: {riga}")
    n_iter += 1
    if len(list(riga)) == len(set(riga)):
        numeri.extend(riga)
        print(f"Riga aggiunta: {riga}")
    

data = np.array(numeri)

print("\nDati prodotti")
print(data)

# reshape in 10 rows of 5 numbers each

data = data.reshape((10, 5))
print("Dati Reshaped:")
print(data)

# Normalizza i valori 
# calcolo media e dev standard
means = data.mean(axis=0)
stds = data.std(axis=0)

# Normalizza i valori
normalized_data = (data - means) / stds
normalized_data = normalized_data.round().astype(int)
print("Dati Normalizzati:")
print(normalized_data)

# Nessun valore deve essere uguale a un altro sulla stessa linea della collezione
for i in range(len(normalized_data)):
    if len(normalized_data[i]) != len(set(normalized_data[i])):
        print(f"Sulla riga {i+1} ci sono almeno due numeri uguali")
        for j in range(len(normalized_data[i])):
            for k in range(len(normalized_data[j])):
                if normalized_data[i][j] == normalized_data[i][k] and j != k:
                    normalized_data[i][k] = np.random.randint(90, 100000)
            
            
        

print(normalized_data)

# Stampa un grafico
plt.plot(normalized_data.flatten())
plt.show()