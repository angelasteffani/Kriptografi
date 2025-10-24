import tkinter as tk
from tkinter import ttk, messagebox

# 🎨 WARNA DAN TEMA
BG_COLOR = "#0B132B"
BTN_COLOR = "#1C2541"
BTN_HOVER = "#3A506B"
TEXT_COLOR = "#6FFFE9"
CONSOLE_COLOR = "#1A1A2E"
TITLE_COLOR = "#5BC0BE"

# 🪟 WINDOW UTAMA
root = tk.Tk()
root.title("Cyber Calculator - ComboBox Mode")
root.geometry("600x430")
root.config(bg=BG_COLOR)
root.resizable(False, False)

# ⚡ HEADER (Judul Estetik)
title_frame = tk.Frame(root, bg=CONSOLE_COLOR, height=60)
title_frame.pack(fill="x")

title_label = tk.Label(
    title_frame,
    text="⚡ CYBER CALCULATOR ⚡",
    font=("Consolas", 20, "bold"),
    fg=TITLE_COLOR,
    bg=CONSOLE_COLOR
)
title_label.pack(pady=10)

# 🔢 FUNGSI HITUNG DENGAN IF
def hitung():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = combo_op.get()

        if op == '+':
            hasil.set(f"[+] Hasil: {a + b}")
        elif op == '-':
            hasil.set(f"[-] Hasil: {a - b}")
        elif op == '*':
            hasil.set(f"[*] Hasil: {a * b}")
        elif op == '/':
            if b != 0:
                hasil.set(f"[/] Hasil: {a / b:.2f}")
            else:
                hasil.set("[!] Tidak bisa dibagi nol!")
        else:
            hasil.set("[!] Pilih operator terlebih dahulu!")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# 🔁 EFEK HASIL BERKEDIP
def blink_result():
    current = console.cget("fg")
    new_color = "#6FFFE9" if current == "#F5F5F5" else "#F5F5F5"
    console.config(fg=new_color)
    root.after(400, blink_result)

# 🧹 RESET & KELUAR
def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    combo_op.set('')
    hasil.set("[*] Hasil akan muncul di sini...")

def keluar():
    if messagebox.askyesno("Keluar", "Yakin mau keluar dari game form?"):
        root.destroy()

# ✏️ LABEL DAN ENTRY
tk.Label(root, text="Input 1 >", font=("Consolas", 12), bg=BG_COLOR, fg=TEXT_COLOR).place(x=150, y=100)
entry1 = tk.Entry(root, font=("Consolas", 12), width=15, fg="#FFFFFF", bg=BTN_COLOR, bd=0, justify="center")
entry1.place(x=250, y=100)

tk.Label(root, text="Input 2 >", font=("Consolas", 12), bg=BG_COLOR, fg=TEXT_COLOR).place(x=150, y=140)
entry2 = tk.Entry(root, font=("Consolas", 12), width=15, fg="#FFFFFF", bg=BTN_COLOR, bd=0, justify="center")
entry2.place(x=250, y=140)

# 🧮 COMBOBOX OPERATOR
tk.Label(root, text="Operator >", font=("Consolas", 12), bg=BG_COLOR, fg=TEXT_COLOR).place(x=150, y=180)
combo_op = ttk.Combobox(root, font=("Consolas", 12), width=10, state="readonly", justify="center")
combo_op['values'] = ('+', '-', '*', '/')
combo_op.place(x=250, y=180)
combo_op.set('')  # kosong di awal

# 💬 AREA HASIL
hasil = tk.StringVar(value="[*] Hasil akan muncul di sini...")
console = tk.Label(root, textvariable=hasil, font=("Consolas", 12),
                   fg="#F5F5F5", bg=CONSOLE_COLOR, width=40, height=3, relief="sunken")
console.place(x=100, y=230)

# 🎮 TOMBOL
def hover_on(e): e.widget.config(bg=BTN_HOVER)
def hover_off(e): e.widget.config(bg=BTN_COLOR)

btn_hitung = tk.Button(root, text="HITUNG [▶]", font=("Consolas", 12, "bold"),
                       bg=BTN_COLOR, fg=TEXT_COLOR, width=14, bd=0, command=hitung)
btn_hitung.place(x=100, y=320)
btn_hitung.bind("<Enter>", hover_on)
btn_hitung.bind("<Leave>", hover_off)

btn_reset = tk.Button(root, text="RESET [↻]", font=("Consolas", 12, "bold"),
                      bg="#6FFFE9", fg="#1B1B2F", width=12, relief="flat", command=reset)
btn_reset.place(x=270, y=320)

btn_exit = tk.Button(root, text="EXIT [X]", font=("Consolas", 12, "bold"),
                     bg="#E84545", fg="white", width=12, relief="flat", command=keluar)
btn_exit.place(x=400, y=320)

# 💡 FOOTER
tk.Label(root, text="Press [Enter] to Calculate | ESC to Exit",
         font=("Consolas", 9), fg="#5BC0BE", bg=BG_COLOR).place(x=180, y=390)

# ⌨️ SHORTCUT
root.bind("<Return>", lambda e: hitung())
root.bind("<Escape>", lambda e: keluar())

# ✨ ANIMASI BERKEDIP
blink_result()

root.mainloop()
