import itertools

print("=== PROGRAM PENGATURAN BUKU DI RAK ===")

n = int(input("Masukkan jumlah buku (n): "))
r = int(input("Masukkan jumlah bagian rak (r): "))

# Buat daftar buku otomatis: Buku1, Buku2, dst
buku = [f"Buku{i+1}" for i in range(n)]

# itertools.product menghasilkan semua kemungkinan penempatan
pengaturan = list(itertools.product(range(1, r + 1), repeat=n))

print(f"\nTerdapat {len(pengaturan)} cara mengatur {n} buku di {r} bagian rak:\n")

for cara in pengaturan:
    for i in range(n):
        print(f"{buku[i]} -> Bagian {cara[i]}")
    print("-" * 30)
