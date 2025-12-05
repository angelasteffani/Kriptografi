from typing import List
import re

sbox_text = """
63 7C 77 7B F2 6B 6F C5 30 01 67 2B FE D7 AB 76
CA 82 C9 7D FA 59 47 F0 AD D4 A2 AF 9C A4 72 C0
B7 FD 93 26 36 3F F7 CC 34 A5 E5 F1 71 D8 31 15
04 C7 23 C3 18 96 05 9A 07 12 80 E2 EB 27 B2 75
09 83 2C 1A 1B 6E 5A A0 52 3B D6 B3 29 E3 2F 84
53 D1 00 ED 20 FC B1 5B 6A CB BE 39 4A 4C 58 CF
D0 EF AA FB 43 4D 33 85 45 F9 02 7F 50 3C 9F A8
51 A3 40 8F 92 9D 38 F5 BC B6 DA 21 10 FF F3 D2
CD 0C 13 EC 5F 97 44 17 C4 A7 7E 3D 64 5D 19 73
60 81 4F DC 22 2A 90 88 46 EE B8 14 DE 5E 0B DB
E0 32 3A 0A 49 06 24 5C C2 D3 AC 62 91 95 E4 79
E7 C8 37 6D 8D D5 4E A9 6C 56 F4 EA 65 7A AE 08
BA 78 25 2E 1C A6 B4 C6 E8 DD 74 1F 4B BD 8B 8A
70 3E B5 66 48 03 F6 0E 61 35 57 B9 86 C1 1D 9E
E1 F8 98 11 69 D9 8E 94 9B 1E 87 E9 CE 55 28 DF
8C A1 89 0D BF E6 42 68 41 99 2D 0F B0 54 BB 16
""".strip()

def parse_sbox(text: str) -> List[int]:
    """Parse teks S-Box (hex) menjadi list int 0..255."""
    parts = re.split(r'\s+', text.strip())
    if len(parts) != 256:
        raise ValueError(f"S-Box harus 256 nilai (hex). Ditemukan {len(parts)}.")
    return [int(x, 16) for x in parts]

SBOX = parse_sbox(sbox_text)
RCON = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]

# Fungsi konversi & utilitas (mirip program 1)
def text_to_bytes(text: str) -> List[int]:
    return [ord(c) for c in text]

def bytes_to_hex(bs: List[int]) -> List[str]:
    return [format(b, '02X') for b in bs]

def to_matrix_4x4(hex_list: List[str]) -> List[List[str]]:
    if len(hex_list) != 16:
        raise ValueError("Harus 16 byte.")
    m = [['']*4 for _ in range(4)]
    for i in range(16):
        r = i % 4
        c = i // 4
        m[r][c] = hex_list[i]
    return m

def xor_matrices(m1: List[List[str]], m2: List[List[str]]) -> List[List[str]]:
    res = [['00']*4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            res[r][c] = format(int(m1[r][c],16) ^ int(m2[r][c],16), '02X')
    return res

# Key expansion berbeda gaya: ambil key sebagai list int
def rot_word(word: List[int]) -> List[int]:
    return word[1:] + word[:1]

def sub_word(word: List[int]) -> List[int]:
    return [SBOX[b] for b in word]

def key_expansion(key_bytes: List[int]) -> List[List[int]]:
    if len(key_bytes) != 16:
        raise ValueError("Key harus 16 byte.")
    key_words = []
    for col in range(4):
        key_words.append([ key_bytes[row + 4*col] for row in range(4) ])
    for i in range(4,44):
        temp = key_words[i-1].copy()
        if i % 4 == 0:
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp[0] ^= RCON[(i//4)-1]
        key_words.append([ temp[j] ^ key_words[i-4][j] for j in range(4) ])
    return key_words

def words_to_matrix(words: List[List[int]]) -> List[List[int]]:
    matrix = [[0]*4 for _ in range(4)]
    for col in range(4):
        for row in range(4):
            matrix[row][col] = words[col][row]
    return matrix

def print_matrix_hex(matrix: List[List[str]], title: str):
    print(f"\n=== {title} ===")
    for r in matrix:
        print(" ".join(r))

def print_key_matrix(matrix: List[List[int]], title: str):
    print(f"\n=== {title} ===")
    for r in matrix:
        print(" ".join(format(x,'02X') for x in r))

# ------------------- Program utama -------------------
def main():
    print("Program AES (S-Box dari gambar/teks) — Konversi & Key Expansion\n")
    # user input
    plaintext = input("Masukkan plaintext (16 karakter): ").strip()
    cipherkey = input("Masukkan cipherkey (16 karakter): ").strip()

    if len(plaintext) != 16 or len(cipherkey) != 16:
        print("Kedua input harus 16 karakter.")
        return

    pt_bytes = text_to_bytes(plaintext)
    key_bytes = text_to_bytes(cipherkey)

    print("\n-- Konversi Plaintext --")
    for i,ch in enumerate(plaintext):
        print(f"{i:02d}: '{ch}' -> dec {pt_bytes[i]} -> hex {format(pt_bytes[i],'02X')} -> bin {format(pt_bytes[i],'08b')}")

    print("\n-- Konversi Cipherkey --")
    for i,ch in enumerate(cipherkey):
        print(f"{i:02d}: '{ch}' -> dec {key_bytes[i]} -> hex {format(key_bytes[i],'02X')} -> bin {format(key_bytes[i],'08b')}")

    hex_pt = bytes_to_hex(pt_bytes)
    hex_key = bytes_to_hex(key_bytes)
    mat_pt = to_matrix_4x4(hex_pt)
    mat_key = to_matrix_4x4(hex_key)
    print_matrix_hex(mat_pt, "PLAINTEXT (HEX) dalam Matriks 4x4")
    print_matrix_hex(mat_key, "CIPHERKEY (HEX) dalam Matriks 4x4")

    mat_xor = xor_matrices(mat_pt, mat_key)
    print_matrix_hex(mat_xor, "HASIL XOR (AddRoundKey)")

    words = key_expansion(key_bytes)
    for r in range(11):
        start = r*4
        chunk = words[start:start+4]
        mat = words_to_matrix(chunk)
        print_key_matrix(mat, f"K{r}")

if __name__ == "__main__":
    main()
