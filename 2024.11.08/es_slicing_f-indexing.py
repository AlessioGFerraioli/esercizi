'''

2024.11.08 11.23
esercizio slicing e fancy indexing

'''


import numpy as np

arr = np.random.randint(10, 50, 20)
print(f"\narray originale:\n{arr}")

sottoarrays = []
sottoarrays.append(arr[:10])
print(f"\nprimi 10 elementi:\n{sottoarrays[0]}")
sottoarrays.append(arr[-5:])
print(f"\nutlimi 5 elementi:\n{sottoarrays[1]}")
sottoarrays.append(arr[5:15])
print(f"\nelementi dal 5 al 15 (escluso):\n{sottoarrays[2]}")


print(f"\nterzo elemento di ogni subarray:")
for arr_ in sottoarrays:
    print(arr_[3])


sottoarrays.append(arr)
sottoarrays[-1][1:10] == 99

print(f"\narray originale :\n {arr}")
print("\nsottoarrays:")
for arr_ in sottoarrays:
    print(arr_)

