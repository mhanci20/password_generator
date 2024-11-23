#!/usr/bin/env python3

import random
import string
import tkinter as tk

def generate_password(length=12,
                      use_lowercase=True,
                      use_uppercase=True,
                      use_numbers=True,
                      use_symbols=True):
    """
    Güçlü bir parola üretir.

    Args:
        length: Parolanın uzunluğu.
        use_lowercase: Küçük harf kullanılıp kullanılmayacağı.
        use_uppercase: Büyük harf kullanılıp kullanılmayacağı.
        use_numbers: Rakam kullanılıp kullanılmayacağı.
        use_symbols: Özel karakter kullanılıp kullanılmayacağı.

    Returns:
        Oluşturulan parola.
    """

    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Tkinter penceresi oluşturma
window = tk.Tk()
window.title("Parola Üretici")

# Etiketler ve giriş kutusu oluşturma
length_label = tk.Label(window, text="Parola Uzunluğu:")
length_entry = tk.Entry(window)

# Kontrol kutuları oluşturma
lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

lowercase_check = tk.Checkbutton(window, text="Küçük Harf", variable=lowercase_var)
uppercase_check = tk.Checkbutton(window, text="Büyük Harf", variable=uppercase_var)
numbers_check = tk.Checkbutton(window, text="Rakam", variable=numbers_var)
symbols_check = tk.Checkbutton(window, text="Özel Karakter", variable=symbols_var)

# Parola gösterme alanı
password_label = tk.Label(window, text="")

def generate_password_and_show():
    length = int(length_entry.get())
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols)
    password_label.config(text=password)

# Üret butonu
generate_button = tk.Button(window, text="Parolayı Üret", command=generate_password_and_show)

# Öğeleri pencereye yerleştirme
length_label.pack()
length_entry.pack()
lowercase_check.pack()
uppercase_check.pack()
numbers_check.pack()
symbols_check.pack()
generate_button.pack()
password_label.pack()

window.mainloop()
