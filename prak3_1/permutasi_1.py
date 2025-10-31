import itertools

def permutasi_menyeluruh(data):
    return list(itertools.permutations(data))

def permutasi_sebagian(data, k):
    return list(itertools.permutations(data, k))

def permutasi_keliling(data):
    if len(data) <= 1:
        return [data]
    pertama = data[0]
    sisanya = list(itertools.permutations(data[1:]))
    return [[pertama] + list(perm) for perm in sisanya]

def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for h in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(h + list(perm))
        hasil = hasil_baru
    return hasil

# ======== Program Utama ========
print("=== PROGRAM PERMUTASI (INPUT DARI KEYBOARD) ===")
print("1. Permutasi Menyeluruh")
print("2. Permutasi Sebagian")
print("3. Permutasi Keliling")
print("4. Permutasi Berkelompok")

pilihan = int(input("Pilih jenis permutasi (1-4): "))

if pilihan == 1:
    data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
    hasil = permutasi_menyeluruh(data)
    print("Hasil Permutasi Menyeluruh:")
    for p in hasil:
        print(p)

elif pilihan == 2:
    data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
    k = int(input("Masukkan jumlah elemen yang diambil (r): "))
    hasil = permutasi_sebagian(data, k)
    print(f"Hasil Permutasi Sebagian (ambil {k} dari {len(data)}):")
    for p in hasil:
        print(p)

elif pilihan == 3:
    data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
    hasil = permutasi_keliling(data)
    print("Hasil Permutasi Keliling:")
    for p in hasil:
        print(p)

elif pilihan == 4:
    jumlah_kelompok = int(input("Masukkan jumlah kelompok: "))
    grup = []
    for i in range(jumlah_kelompok):
        anggota = input(f"Masukkan elemen untuk kelompok {i+1} (pisahkan spasi): ").split()
        grup.append(anggota)
    hasil = permutasi_berkelompok(grup)
    print("Hasil Permutasi Berkelompok:")
    for p in hasil:
        print(p)
else:
    print("Pilihan tidak valid.")
