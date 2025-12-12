import math

# ------------------ LANGKAH 1-5: GENERATE KUNCI ------------------

p = 17
q = 11
e = 7

print("===== LATIHAN 1: RSA (p=17, q=11, e=7) =====\n")

print("1. Pilih Bilangan Prima p dan q")
print(f"   p = {p}")
print(f"   q = {q}")

# 2. Hitung modulus n
n = p * q
print("\n2. Hitung Modulus n = p × q")
print(f"   n = {p} × {q} = {n}")

# 3. Hitung Euler phi(n)
phi_n = (p - 1) * (q - 1)
print("\n3. Hitung Fungsi Euler φ(n) = (p−1)(q−1)")
print(f"   φ(n) = (17−1)(11−1) = 16 × 10 = {phi_n}")

# 4. Pembuktian GCD(e, φ(n)) = 1
print("\n4. Pembuktian GCD(e, φ(n)) = 1")
print("   Menggunakan Euclidean Algorithm:")
a, b = phi_n, e

print(f"   GCD({e}, {phi_n}) = ?")

# proses pembagian
A = 160
B = 7
print(f"   160 = 22 × 7 + 6")
print(f"   7 = 1 × 6 + 1")
print(f"   6 = 6 × 1 + 0")
print("   Sisa terakhir = 1 → GCD = 1 (Memenuhi Syarat)")

# 5. Hitung nilai d menggunakan metode di PDF
print("\n5. Mencari Eksponen Privat d")
print("   Menggunakan Persamaan: 7d - 160k = 1")
print("   Uji k = 1 → 7d - 160 = 1 → 7d = 161 → d = 23")

d = 23
print(f"   Nilai d = {d}")

print("\nKUNCI PUBLIK  : (e, n) = ({e}, {n})")
print(f"KUNCI PRIVAT  : (d, n) = ({d}, {n})")

# ===================== ENKRIPSI =====================

def rsa_encrypt_ascii(message):
    print("\n===== PROSES ENKRIPSI =====")
    print("Plaintext | ASCII | Enkripsi C = M^e mod n")
    print("-------------------------------------------")

    ciphertext = []

    for ch in message:
        M = ord(ch)
        C = pow(M, e, n)

        print(f"   {ch:3}     |  {M:4} | {M}^{e} mod {n} = {C}")

        ciphertext.append(C)

    return ciphertext

# ===================== DEKRIPSI =====================

def rsa_decrypt(cipher_list):
    print("\n===== PROSES DEKRIPSI =====")
    print("Cipher | Dekripsi M = C^d mod n | ASCII | Huruf")
    print("------------------------------------------------")

    plaintext = ""

    for C in cipher_list:
        M = pow(C, d, n)
        plaintext += chr(M)

        print(f"   {C:4} | {C}^{d} mod {n} = {M:4} |  {M:4} | {chr(M)}")

    return plaintext


# ===================== MAIN =====================

text = input("\nMasukkan Plaintext: ")

cipher_list = rsa_encrypt_ascii(text)
print("\nCiphertext (angka):", cipher_list)

plain = rsa_decrypt(cipher_list)
print("\nPlaintext Kembali :", plain)
