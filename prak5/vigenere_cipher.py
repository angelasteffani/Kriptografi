class VigenereCipher:
    def __init__(self, text, key):
        self.text = text.upper().replace(" ", "")
        self.key = key.upper().replace(" ", "")
        self.key = self.generate_key()

    def generate_key(self):
        key = list(self.key)
        if len(self.text) == len(key):
            return "".join(key)
        else:
            for i in range(len(self.text) - len(key)):
                key.append(key[i % len(self.key)])
        return "".join(key)

    def encrypt(self):
        print("\n=== PROSES ENKRIPSI (DETAIL) ===")
        print("No | Huruf Teks | Huruf Kunci | Shift | Hasil")
        print("---------------------------------------------")

        cipher_text = ""
        for i in range(len(self.text)):
            t = ord(self.text[i]) - 65
            k = ord(self.key[i]) - 65
            shift = (t + k) % 26
            hasil = chr(shift + 65)

            print(f"{i+1:2} |     {self.text[i]}      |     {self.key[i]}      |   {k:4} |   {hasil}")

            cipher_text += hasil
        return cipher_text

    def decrypt(self, cipher_text):
        print("\n=== PROSES DEKRIPSI (DETAIL) ===")
        print("No | Huruf Cipher | Huruf Kunci | Shift | Hasil")
        print("-----------------------------------------------")

        plain_text = ""
        for i in range(len(cipher_text)):
            c = ord(cipher_text[i]) - 65
            k = ord(self.key[i]) - 65
            shift = (c - k + 26) % 26
            hasil = chr(shift + 65)

            print(f"{i+1:2} |      {cipher_text[i]}      |     {self.key[i]}      |   {k:4} |   {hasil}")

            plain_text += hasil
        return plain_text


# ================= MAIN PROGRAM ==================
print("===== PROGRAM VIGENERE CIPHER (PBO) =====")
text = input("Masukkan Teks     : ")
key = input("Masukkan Kunci    : ")

cipher = VigenereCipher(text, key)

# ENKRIPSI
encrypted = cipher.encrypt()
print("\nCiphertext        :", encrypted)

# DEKRIPSI
decrypted = cipher.decrypt(encrypted)
print("Plaintext Kembali :", decrypted)
