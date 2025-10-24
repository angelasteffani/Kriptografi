print("=== Kalkulator Sederhana ===")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
op = input("Masukkan operator (+, -, *, /): ")

ops = {
    '+': a + b,
    '-': a - b,
    '*': a * b,
    '/': a / b if b != 0 else "Tidak bisa dibagi nol"
}

print("Hasil:", ops.get(op, "Operator tidak valid"))
