# =====================================
# ELGAMAL ENKRIPSI & DEKRIPSI
# VERSI STABIL + MANUAL + TABEL
# =====================================

# ---------- INPUT ----------
p = int(input("Masukkan p (prima): "))
g = int(input("Masukkan g (generator): "))
x = int(input("Masukkan kunci privat x: "))
k = int(input("Masukkan nilai k (acak): "))
plaintext = input("Masukkan plaintext (nama): ").strip().upper()

# ---------- KUNCI PUBLIK ----------
y = pow(g, x, p)

print("\n=== PARAMETER ===")
print(f"p = {p}")
print(f"g = {g}")
print(f"x = {x}")
print(f"k = {k}")
print(f"Plaintext = {plaintext}")

# ---------- KONVERSI ASCII ----------
ascii_list = [ord(c) for c in plaintext]

print("\n=== KONVERSI PLAINTEXT KE ASCII ===")
for c, m in zip(plaintext, ascii_list):
    print(f"{c} -> {m}")

# ---------- KUNCI PUBLIK (DIPINDAHKAN KE SINI) ----------
print("\n=== KUNCI PUBLIK ===")
print("y = g^x mod p")
print(f"y = {g}^{x} mod {p}")
print(f"y = {y}")

# ---------- HITUNG a dan y^k ----------
a = pow(g, k, p)
yk = pow(y, k, p)

print("\n=== NILAI PENDUKUNG ===")
print(f"a = g^k mod p = {g}^{k} mod {p} = {a}")
print(f"y^k mod p = {y}^{k} mod {p} = {yk}")

# ---------- ENKRIPSI ----------
print("\n=== PROSES ENKRIPSI (MANUAL) ===")
print("Rumus: b = (y^k × m) mod p\n")

print("-" * 85)
print(f"{'No':<3} {'Huruf':<6} {'m':<6} {'y^k×m':<12} {'(y^k×m) mod p':<18} {'Cipher (a,b)':<15}")
print("-" * 85)

cipher = []

for i, m in enumerate(ascii_list):
    kali = yk * m
    b = kali % p
    cipher.append((a, b))
    print(f"{i+1:<3} {plaintext[i]:<6} {m:<6} {kali:<12} {kali} mod {p} = {b:<8} ({a},{b})")

# ---------- DEKRIPSI ----------
print("\n=== PROSES DEKRIPSI (SANGAT MANUAL) ===")
print("Rumus: m = (b × (a^x)^-1) mod p\n")

ax = pow(a, x, p)
print(f"Langkah 1: a^x mod p = {a}^{x} mod {p} = {ax}")

ax_inv = pow(ax, p - 2, p)
print(f"Langkah 2: invers(a^x) = {ax}^({p}-2) mod {p} = {ax_inv}")

print("\nLangkah 3: Hitung m tiap ciphertext")
print("-" * 80)
print(f"{'No':<3} {'b':<6} {'b×inv':<12} {'(b×inv) mod p':<18} {'m (ASCII)':<10}")
print("-" * 80)

hasil_ascii = []

for i, (_, b) in enumerate(cipher):
    kali = b * ax_inv
    m_dec = kali % p
    hasil_ascii.append(m_dec)
    print(f"{i+1:<3} {b:<6} {kali:<12} {kali} mod {p} = {m_dec:<8}")

print("\n=== HASIL AKHIR ===")
print("ASCII hasil dekripsi:")
print(hasil_ascii)
print("\nKonversi ke huruf dilakukan MANUAL menggunakan tabel ASCII.")
