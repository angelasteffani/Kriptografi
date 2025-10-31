import itertools

def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

def kombinasi(n, r):
    if r > n:
        return 0
    faktorial_n = faktorial(n)
    faktorial_r = faktorial(r)
    faktorial_n_r = faktorial(n - r)
    return faktorial_n // (faktorial_r * faktorial_n_r)

# ======== Program Utama ========
print("=== PROGRAM KOMBINASI DENGAN INISIAL HURUF ===")

# Input dari pengguna
huruf = input("Masukkan inisial huruf (pisahkan dengan spasi): ").split()
n = len(huruf)
r = int(input("Masukkan jumlah huruf yang dipilih (r): "))

# Hitung jumlah kombinasi secara matematis
jumlah = kombinasi(n, r)
print(f"\nJumlah kombinasi C({n}, {r}) adalah: {jumlah}\n")

# Tampilkan semua hasil kombinasi aktual
hasil_kombinasi = list(itertools.combinations(huruf, r))
print("Hasil kombinasi huruf:")
for kombinasi_huruf in hasil_kombinasi:
    print(kombinasi_huruf)
