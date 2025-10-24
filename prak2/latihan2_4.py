# Program Kalkulator Modern (tanpa form)

print("=== KALKULATOR ARITMATIKA MODERN ===")
print("Pilih operator yang diinginkan:")
print("1. +  (Penjumlahan)")
print("2. -  (Pengurangan)")
print("3. *  (Perkalian)")
print("4. /  (Pembagian)")
print("=====================================")

# Input nilai
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Input operator seperti combo box
operator = input("Pilih operator (+, -, *, /): ")

# Proses perhitungan
if operator == '+':
    hasil = angka1 + angka2
    operasi = "Penjumlahan"
elif operator == '-':
    hasil = angka1 - angka2
    operasi = "Pengurangan"
elif operator == '*':
    hasil = angka1 * angka2
    operasi = "Perkalian"
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        operasi = "Pembagian"
    else:
        print("⚠️ Error: Tidak bisa membagi dengan nol!")
        exit()
else:
    print("⚠️ Operator tidak valid! Silakan pilih +, -, *, atau /.")
    exit()

# Output hasil
print("\n🔹 Hasil", operasi, "adalah:", hasil)
print("=====================================")
print("Terima kasih sudah menggunakan Kalkulator Modern 💻✨")
