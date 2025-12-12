# ===================== RSA LANGKAH PELAN SESUAI PPT =====================

p = 53
q = 199
e = 193   # bilangan prima

print("===== PROGRAM RSA (LANGKAH BERTAHAP SESUAI PPT) =====\n")

# -------------------------------------------------------
# 1. Menentukan p dan q
# -------------------------------------------------------
print("LANGKAH 1: Menentukan p dan q")
print(f"p = {p}")
print(f"q = {q}\n")

# -------------------------------------------------------
# 2. Hitung n = p × q
# -------------------------------------------------------
print("LANGKAH 2: Hitung n = p × q")
n = p * q
print(f"n = {p} × {q} = {n}\n")

# -------------------------------------------------------
# 3. Hitung φ(n) = (p-1)(q-1) PELAN-PELAN SESUAI PPT
# -------------------------------------------------------
print("LANGKAH 3: Hitung φ(n) = (p - 1)(q - 1)")
p1 = p - 1
q1 = q - 1
print(f"p - 1 = {p} - 1 = {p1}")
print(f"q - 1 = {q} - 1 = {q1}")

phi = p1 * q1
print(f"φ(n) = {p1} × {q1} = {phi}\n")

# -------------------------------------------------------
# 4. Memeriksa gcd(e, φ(n)) dengan LANGKAH EUCLIDIAN
# -------------------------------------------------------
print("LANGKAH 4: Memeriksa gcd(e, φ(n)) menggunakan Algoritma Euclidean")
print(f"gcd({e}, {phi})\n")

A, B = phi, e
step = 1
while B != 0:
    q = A // B
    r = A % B
    print(f"Step {step}: {A} = {q} × {B} + {r}")
    A, B = B, r
    step += 1

print("\nKarena sisa terakhir = 1, maka gcd = 1 (VALID)\n")

# -------------------------------------------------------
# 5. Mencari d dengan Extended Euclidean (Back Substitution)
# -------------------------------------------------------
print("LANGKAH 5: Mencari d (invers e mod φ) dengan Back Substitution")

def ext_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    x2, y2, g = ext_gcd(b, a % b)
    x = y2
    y = x2 - (a // b) * y2
    return (x, y, g)

x, y, g = ext_gcd(e, phi)
d = x % phi

print(f"Hasil persamaan: {e}*({x}) + {phi}*({y}) = {g}")
print(f"Maka d = {x} mod {phi} = {d}\n")

print(f"Kunci Publik  = ({e}, {n})")
print(f"Kunci Privat  = ({d}, {n})\n")

# -------------------------------------------------------
# 6. ENKRIPSI – tampilkan langkah seperti PPT
# -------------------------------------------------------
plaintext = "ANGELASTEFFA"
print("LANGKAH 6: ENKRIPSI plaintext =", plaintext)
print("No | Huruf | ASCII | C = M^e mod n")
print("------------------------------------")

cipher = []
for i, ch in enumerate(plaintext, start=1):
    M = ord(ch)
    C = pow(M, e, n)
    cipher.append(C)
    print(f"{i:2} |   {ch}   |  {M}   |  {M}^{e} mod {n} = {C}")

print("\nCiphertext =", cipher, "\n")

# -------------------------------------------------------
# 7. DEKRIPSI – tampilkan langkah seperti PPT
# -------------------------------------------------------
print("LANGKAH 7: DEKRIPSI")
print("No | C       | M = C^d mod n | ASCII | Huruf")
print("---------------------------------------------")

result = ""
for i, C in enumerate(cipher, start=1):
    M = pow(C, d, n)
    result += chr(M)
    print(f"{i:2} | {C:7} | {C}^{d} mod {n} = {M:5} | {M:5} | {chr(M)}")

print("\nPlaintext kembali =", result)
print("\n===================== SELESAI =====================\n")
