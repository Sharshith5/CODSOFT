import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(entry_length.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Info", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=5)

label_password = tk.Label(root, text="Generated Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root)
entry_password.pack(pady=5)

button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
button_copy.pack(pady=5)

root.mainloop()
