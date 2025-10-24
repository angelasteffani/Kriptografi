biner = input("Masukkan bilangan biner: ")
desimal = int(biner, 2)
heksa = hex(desimal)

print("\n== HASIL KONVERSI ==")
print(f"Biner      : {biner}")
print(f"Desimal    : {desimal}")
print(f"Hexadesimal: {heksa[2:].upper()}")
