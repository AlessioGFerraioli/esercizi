'''
Create 2 array numpy:

- Un array unidimensionale di numeri casuali compresi tra 0 e 1;
- Un array bidimensionale di dimensione 3x3 con valori interi casuali.

parte 2

Create 2 array bidimensionali numpy 4x4 con valori interi casuali ed eseguite le seguenti operazioni:

- Restituite la somma di tutti gli elementi dei singoli array che si trovano nell'ultima riga dalla seconda colonna in poi;
- Unite i 2 array secondo l'asse 1.

parte3 

Create 1 array unidimensionale con 50 valori randomici compresi tra 1 e 1.000 e fate i seguenti calcoli:

- Calcolo della media;
Calcolo della moda;
-Calcolo della deviazione standard;
- Trasformatelo in un array 5 X 10
'''

import numpy as np

print(np.random.random(5))

print(np.random.randint(0,100,(3,3)))

print("fine parte 1\n----------------------------------")
A = np.random.randint(0,100,(4,4))
B = np.random.randint(0,100,(4,4))

print(A)
print("---------")
print(B)
print("---------")
#- Restituite la somma di tutti gli elementi dei singoli array 
# che si trovano nell'ultima riga dalla seconda colonna in poi;
print("Ultima riga dalla seconda colonna:")
print(A[-1][1:])
print(B[-1][1:])
print(f"Somma = {A[-1][1:]+B[-1][1:]}")

#- Unite i 2 array secondo l'asse 1.
print("Unione dei due array secondo asse 1:")
C = np.concatenate((A,B), axis=1)
print(C)


'''

parte3 

Create 1 array unidimensionale con 50 valori randomici compresi tra 1 e 1.000 e fate i seguenti calcoli:

- Calcolo della media;
Calcolo della moda;
-Calcolo della deviazione standard;
- Trasformatelo in un array 5 X 10
'''

from scipy import stats 

A = np.random.randint(1,1000,50)

media = np.average(A)
print(f"media : {media}")
devsta = np.std(A)
print(f"std : {devsta}")
moda = stats.mode(A)[0]
print(f"moda : {moda}")