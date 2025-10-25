# Program mengurutkan 3 data dari terkecil ke terbesar (tanpa sort)
print("program mengurutkan data")
# Input data
a = int(input("bilangan ke-1:"))
b = int(input("bilangan ke-2: "))
c = int(input("bilangan ke-3: "))

# Proses pengurutan menggunakan if
if a <= b and a <= c:
    if b <= c:
        print("Urutan dari terkecil:", a, b, c)
    else:
        print("Urutan dari terkecil:", a, c, b)
elif b <= a and b <= c:
    if a <= c:
        print("Urutan dari terkecil:", b, a, c)
    else:
        print("Urutan dari terkecil:", b, c, a)
else:
    if a <= b:
        print("Urutan dari terkecil:", c, a, b)
    else:
        print("Urutan dari terkecil:", c, b, a)
