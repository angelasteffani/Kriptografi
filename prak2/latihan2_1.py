import tkinter as tk
from tkinter import messagebox
import operator

# =============================
#       KONFIGURASI DASAR
# =============================
root = tk.Tk()
root.title("🧮 Kalkulator Modern - Angela Steffani")
root.geometry("420x400")
root.configure(bg="#F9FAFB")
root.resizable(False, False)

# =============================
#       TEMA DAN GAYA
# =============================
WARNA_BG = "#F9FAFB"
WARNA_CARD = "#E3F2FD"
WARNA_BTN = "#1E88E5"
WARNA_RESET = "#FFB300"
WARNA_KELUAR = "#E53935"
WARNA_TULISAN = "#263238"

FONT_JUDUL = ("Segoe UI", 16, "bold")
FONT_LABEL = ("Segoe UI", 11)
FONT_BTN = ("Segoe UI", 10, "bold")

# =============================
#       HEADER
# =============================
judul = tk.Label(
    root,
    text="💡 Kalkulator Aritmatika Modern 💡",
    bg="#1565C0",
    fg="white",
    font=FONT_JUDUL,
    width=35,
    pady=12
)
judul.pack(pady=10)

# =============================
#       FRAME UTAMA
# =============================
frame = tk.Frame(root, bg=WARNA_CARD, padx=20, pady=20)
frame.pack(pady=10)

# Input Nilai A
tk.Label(frame, text="Masukkan Nilai A:", font=FONT_LABEL, bg=WARNA_CARD).grid(row=0, column=0, sticky="w", pady=8)
entry_a = tk.Entry(frame, width=18, font=FONT_LABEL, justify="center", relief="solid", bd=1)
entry_a.grid(row=0, column=1, padx=10)

# Input Nilai B
tk.Label(frame, text="Masukkan Nilai B:", font=FONT_LABEL, bg=WARNA_CARD).grid(row=1, column=0, sticky="w", pady=8)
entry_b = tk.Entry(frame, width=18, font=FONT_LABEL, justify="center", relief="solid", bd=1)
entry_b.grid(row=1, column=1, padx=10)

# Pilih Operator
tk.Label(frame, text="Pilih Operator:", font=FONT_LABEL, bg=WARNA_CARD).grid(row=2, column=0, sticky="w", pady=8)
operator_var = tk.StringVar(value="+")
menu_operator = tk.OptionMenu(frame, operator_var, "+", "-", "*", "/")
menu_operator.config(font=FONT_LABEL, bg="#BBDEFB", relief="flat", width=10)
menu_operator.grid(row=2, column=1, padx=5)

# Label Hasil
label_hasil = tk.Label(frame, text="💬 Hasil akan muncul di sini", bg=WARNA_CARD, fg="#37474F", font=("Segoe UI", 11, "italic"))
label_hasil.grid(row=3, column=0, columnspan=2, pady=15)

# =============================
#       FUNGSI PROGRAM
# =============================
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

def hitung():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        op = operator_var.get()
        if op not in ops:
            messagebox.showwarning("Peringatan", "Pilih operator yang valid!")
            return
        hasil = ops[op](a, b)
        label_hasil.config(
            text=f"✨ Hasil: {a} {op} {b} = {hasil:.2f} ✨",
            fg="#0D47A1"
        )
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Tidak bisa membagi dengan nol!")

def reset():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    operator_var.set("+")
    label_hasil.config(text="💬 Hasil akan muncul di sini", fg="#37474F")

def keluar():
    if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar?"):
        root.destroy()

# =============================
#       TOMBOL-TOMBOL
# =============================
frame_btn = tk.Frame(root, bg=WARNA_BG)
frame_btn.pack(pady=10)

def hover_in(event, warna):
    event.widget.config(bg=warna)

def hover_out(event, warna):
    event.widget.config(bg=warna)

btn_hitung = tk.Button(
    frame_btn, text="Hitung", bg=WARNA_BTN, fg="white",
    font=FONT_BTN, width=10, relief="flat", command=hitung
)
btn_hitung.grid(row=0, column=0, padx=10)
btn_hitung.bind("<Enter>", lambda e: hover_in(e, "#42A5F5"))
btn_hitung.bind("<Leave>", lambda e: hover_out(e, WARNA_BTN))

btn_reset = tk.Button(
    frame_btn, text="Reset", bg=WARNA_RESET, fg="black",
    font=FONT_BTN, width=10, relief="flat", command=reset
)
btn_reset.grid(row=0, column=1, padx=10)
btn_reset.bind("<Enter>", lambda e: hover_in(e, "#FFD54F"))
btn_reset.bind("<Leave>", lambda e: hover_out(e, WARNA_RESET))

btn_keluar = tk.Button(
    frame_btn, text="Keluar", bg=WARNA_KELUAR, fg="white",
    font=FONT_BTN, width=10, relief="flat", command=keluar
)
btn_keluar.grid(row=0, column=2, padx=10)
btn_keluar.bind("<Enter>", lambda e: hover_in(e, "#EF5350"))
btn_keluar.bind("<Leave>", lambda e: hover_out(e, WARNA_KELUAR))

# =============================
#       FOOTER
# =============================
footer = tk.Label(
    root,
    text="© 2025 | Dibuat oleh Angela Steffani | Kalkulator Modern",
    bg=WARNA_BG,
    fg="#607D8B",
    font=("Segoe UI", 9, "italic")
)
footer.pack(side="bottom", pady=10)

# Jalankan Program
root.mainloop()
