'''
crea un array numpy utilizzando arange
e verifica il tipo di dat con dtype
e la forma dell'array con shape
'''


class FloatArr:

    def __init__(self):
        import numpy as np
        self.__arr = np.arange(10,49)
        print("Instanziato array.")

    def print_type(self):
        print(f"\ndtype = {self.get_arr().dtype}")

    def get_arr(self):
        return self.__arr
    
    def convert_to_float(self):
        print("\nConversione in float64. ")
        return self.get_arr().astype(float)
    
    def print_shape(self):
        print(f"\nshape : {self.get_arr().shape}")


arr = FloatArr()
arr.print_type()
arr.convert_to_float()
arr.print_type()
arr.print_shape()