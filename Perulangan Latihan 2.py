import random

# Input jumlah bilangan
n = int(input("masukkan jumlah n : "))

i = 2
while i < n:
    for j in range(1):
        bil = random.random()  # menghasilkan angka acak antara 0 - 1
        if bil < 0.5:
            print(bil)
            i += 1
