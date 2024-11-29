import numpy as np

data = np.random.randint(1, 100, size=(5,))

print(data[0])

data[0] += .1

print(data[0])