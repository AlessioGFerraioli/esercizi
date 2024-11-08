'''

2024.11.08 11.23
esercizio slicing e fancy indexing

'''


import numpy as np



class ArraySlicer:
    
    def __init__(self, low, high, size):
        self.__arr = self.generate_random_array(self,low,high,size)

    def generate_random_array(self, low, high, size):
        return np.random.randint(10, 50, 20)
    
    def print_array(self):
        print(f"Array:\nself.get_arr()")
    
    def print_shape(self):
        print(f"\nshape : {self.get_arr().shape}")

    def get_arr(self):
        return self.__arr
    
    def primi_n_elementi(self, n):
        return self.get_array()[:n]
    
    def ultimi_n_elementi(self, n):
        return self.get_array()[-n:]
    
    def elementi_da_m_a_n(self, m, n):
        return self.get_array()[m:n]
    
    def n_esimo_elemento(self, n):
        return self.get_array()[n]

    def setta_valori_uguali_a(self, start, stop, valore):
        return self.get_array()[n][start:stop] = valore

    


arr = ArraySlicer(10,50,20)

print(f"\narray originale:")
arr.print_array()


sottoarrays = []

sottoarrays.append(arr.primi_n_elementi(10))
print(f"\nprimi 10 elementi:\n{sottoarrays[0]}")
sottoarrays.append(arr[-5:])
print(f"\nutlimi 5 elementi:\n{sottoarrays[1]}")
sottoarrays.append(arr[5:15])
print(f"\nelementi dal 5 al 15 (escluso):\n{sottoarrays[2]}")


print(f"\nterzo elemento di ogni subarray:")
for arr_ in sottoarrays:
    print(arr_[3])


sottoarrays.append(arr)
sottoarrays[-1][1:10] = 99

print(f"\narray originale :\n {arr}")
print("\nsottoarrays:")
for arr_ in sottoarrays:
    print(arr_)