'''

2024.11.08 11.23
esercizio slicing e fancy indexing

'''


import numpy as np



class ArraySlicer:
    
    def __init__(self, low, high, size):
        self.__arr = self.generate_random_array(low,high,size)

    def generate_random_array(self, low, high, size):
        return np.random.randint(10, 50, 20)
    
    def print_array(self):
        print(f"Array:\n{self.get_arr()}")
    
    def print_shape(self):
        print(f"\nshape : {self.get_arr().shape}")

    def get_arr(self):
        return self.__arr
    
    def primi_n_elementi(self, n):
        return self.get_arr()[:n]
    
    def ultimi_n_elementi(self, n):
        return self.get_arr()[-n:]
    
    def elementi_da_m_a_n(self, m, n):
        return self.get_arr()[m:n]
    
    def n_esimi_elementi(self, lista_di_array, n):
        lista_n_esimi_elementi = [self.get_arr()]
        for arr_ in lista_di_array:
            n_elemento = arr_[n]
            lista_n_esimi_elementi.append(n_elemento)
        return lista_n_esimi_elementi
    
    def setta_valori_uguali_a(self, start, stop, valore):
        self.get_arr()[start:stop] = valore
        return self.get_arr()

    def every_nth_elemento(self, n):
        return self.get_arr()[::3]
    


arr = ArraySlicer(10,50,20)

print("\narray originale :")
arr.print_array()



sottoarrays = []

sottoarrays.append(arr.primi_n_elementi(10))
print(f"\nprimi 10 elementi:\n{sottoarrays[0]}")
sottoarrays.append(arr.ultimi_n_elementi(5))
print(f"\nutlimi 5 elementi:\n{sottoarrays[1]}")
sottoarrays.append(arr.elementi_da_m_a_n(5,15))
print(f"\nelementi dal 5 al 15 (escluso):\n{sottoarrays[2]}")
sottoarrays.append(arr.every_nth_elemento(3))
print(f"\nogni terzo elemento:\n{sottoarrays[3]}")


print("Cambiati valori a 99: ")
arr.print_array()



print("\nsottoarrays:")
for arr_ in sottoarrays:
    print(arr_)