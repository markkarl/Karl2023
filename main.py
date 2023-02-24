import random
import tkinter as tk
from tkinter import scrolledtext, Tk, Text
from vigenere_cipher import table3, vigerenencrypt, decrypt
from row_cipher import rowencrypt, rowdecrypt
from product_cipher import productencrypt, productdecrypt

def encrypt_decrypt():
    global encrypted, decrypted, encrypted2, decrypted2, encrypted3, decrypted3

    plaintext = plaintext_input.get("1.0", tk.END).strip()
    table = []
    hashmap = {}
    table3(table, hashmap)

    # Vigenere
    key = ""
    plain = ""
    for i in range(len(plaintext)):
        y = random.randint(0, 35)
        key += hashmap[y]
        if plaintext[i] == " ":
            key = key[:-1]
        else:
            plain += plaintext[i]
    encrypted = vigerenencrypt(plain, key, hashmap, table)
    decrypted = decrypt(encrypted, key, hashmap, table)

    vigenere_encrypted.config(state='normal')
    vigenere_encrypted.delete("1.0", tk.END)
    vigenere_encrypted.insert(tk.END, encrypted)
    vigenere_encrypted.config(state='disabled')

    vigenere_decrypted.config(state='normal')
    vigenere_decrypted.delete("1.0", tk.END)
    vigenere_decrypted.insert(tk.END, decrypted)
    vigenere_decrypted.config(state='disabled')
    # Row
    key2 = 0
    num = round(len(plaintext) / 5)
    for i in range(num):
        y = random.randint(1, num)
        if key2 == 0:
            key2 = []
        else:
            while y in key2:
                y = random.randint(1, num)
        key2.append(y)
    encrypted2 = rowencrypt(encrypted, key2)
    decrypted2 = rowdecrypt(encrypted2, key2)

    row_encrypted.config(state='normal')
    row_encrypted.delete("1.0", tk.END)
    row_encrypted.insert(tk.END, encrypted2)
    row_encrypted.config(state='disabled')

    row_decrypted.config(state='normal')
    row_decrypted.delete("1.0", tk.END)
    row_decrypted.insert(tk.END, decrypted2)
    row_decrypted.config(state='disabled')
    # Product
    key3 = 0
    for i in range(len(encrypted2)):
        y = random.randint(1, len(encrypted2))
        if key3 == 0:
            key3 = []
        else:
            while y in key3:
                y = random.randint(1, len(encrypted2))
        key3.append(y)
    encrypted3 = productencrypt(encrypted2, key3, hashmap)
    decrypted3 = productdecrypt(encrypted3, key3, hashmap)

    product_encrypted.config(state='normal')
    product_encrypted.delete("1.0", tk.END)
    product_encrypted.insert(tk.END, encrypted3)
    product_encrypted.config(state='disabled')

    product_decrypted.config(state='normal')
    product_decrypted.delete("1.0", tk.END)
    product_decrypted.insert(tk.END, decrypted3)
    product_decrypted.config(state='disabled')

    result.config(state='normal')
    result.delete("1.0", tk.END)
    result.insert(tk.END, encrypted3)
    result.config(state='disabled')
root = tk.Tk()
root.title("Encryption/Decryption Tool")
global encrypted, decrypted, encrypted2, decrypted2, encrypted3, decrypted3
frame = tk.Frame(root, bg="grey")
frame.pack(padx=10, pady=10)

plaintext_label = tk.Label(frame, text="Enter plaintext:", font=("Arial", 20, "bold"), bg="grey")
plaintext_label.grid(row=0, column=0, sticky="w")

plaintext_input = tk.Text(frame, wrap=tk.WORD, width=40, height=2,font= ("Arial", 10, "bold"))
plaintext_input.grid(row=1, column=0, padx=5, pady=5)

tk.Label(frame, text=f"Result:",font= ("Arial", 15, "bold"),bg="grey").grid(row=3, column=0, sticky="w")
result = tk.Text(frame, wrap=tk.WORD, width=30, height=2, state='disabled',font= ("Arial", 10, "bold"))
result.grid(row=4, column=0, padx=5, pady=5)

encrypt_button = tk.Button(frame, text="Encrypt/Decrypt", command=encrypt_decrypt, font=("Arial", 15, "bold"), bg="#009FBD", bd=3)
encrypt_button.grid(row=2, column=0, pady=10)

tk.Label(frame, text=f"Vigenere Encrypted",font= ("Arial", 15, "bold"),bg="grey").grid(row=0, column=1, sticky="s")
vigenere_encrypted = tk.Text(frame, wrap=tk.WORD, width=40, height=2, state='disabled',font= ("Arial", 10, "bold"))
vigenere_encrypted.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text=f"Vigenere Decrypted",font= ("Arial", 15, "bold"),bg="grey").grid(row=2, column=1, sticky="s")
vigenere_decrypted = tk.Text(frame, wrap=tk.WORD, width=40, height=2, state='disabled',font= ("Arial", 10, "bold"))
vigenere_decrypted.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text=f"Row Encrypted",font= ("Arial", 15, "bold"),bg="grey").grid(row=4, column=1, sticky="s")
row_encrypted = tk.Text(frame, wrap=tk.WORD, width=40, height=2, state='disabled',font= ("Arial", 10, "bold"))
row_encrypted.grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame, text=f"Row Decrypted",font= ("Arial", 15, "bold"),bg="grey").grid(row=6, column=1, sticky="s")
row_decrypted = tk.Text(frame, wrap=tk.WORD, width=40, height=2, state='disabled',font= ("Arial", 10, "bold"))
row_decrypted.grid(row=7, column=1, padx=5, pady=5)

tk.Label(frame, text=f"Product Encrypted",font= ("Arial", 15, "bold"),bg="grey").grid(row=8, column=1, sticky="s")
product_encrypted = tk.Text(frame, wrap=tk.WORD, width=40, height=2, state='disabled',font= ("Arial", 10, "bold"))
product_encrypted.grid(row=9, column=1, padx=5, pady=5)

tk.Label(frame, text=f"Product Decrypted",font= ("Arial", 15, "bold"),bg="grey").grid(row=10, column=1, sticky="s")
product_decrypted = tk.Text(frame, wrap=tk.WORD, width=40, height=2, state='disabled',font= ("Arial", 10, "bold"))
product_decrypted.grid(row=11, column=1, padx=5, pady=5)

root.mainloop()