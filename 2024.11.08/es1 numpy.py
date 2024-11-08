'''
2024.11.08 10:56
es1 numpy
crea un array numpy utilizzando arange
e verifica il tipo di dat con dtype
e la forma dell'array con shape
'''

import numpy as np

class FloatArr:

    def __init__(self, start, stop):
        self.__arr = np.arange(start,stop)
        print("Instanziato array.")

    def print_array(self):
        print(f"Array:\nself.get_arr()")

    def print_type(self):
        print(f"\ndtype = {self.get_arr().dtype}")
    
    def convert_to_float(self):
        print("\nConversione in float64. ")
        return self.get_arr().astype(float)
    
    def print_shape(self):
        print(f"\nshape : {self.get_arr().shape}")

    def get_arr(self):
        return self.__arr

arr = FloatArr(10, 50)
arr.print_array()
arr.print_type()
arr.convert_to_float()
arr.print_type()
arr.print_shape()