import secrets
import string
import tkinter as tk
from tkinter import ttk


def generate_password():
    length_str = length_entry.get()
    if length_str.isdigit():
        length = int(length_str)
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    elif not length_str:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Используйте цифры!")
    else:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Используйте цифры!")


window = tk.Tk()
window.title("Password Generator Ver. 0.1 beta.")
window.geometry("400x200")
window.resizable(False, False)

length_label = ttk.Label(window, text="Длина пароля:")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = ttk.Entry(window, validate='key')
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.configure(validatecommand=(
    length_entry.register(lambda val: val.isdigit()), '%P'))

generate_button = ttk.Button(
    window, text="Сгенерировать пароль", command=generate_password, style='my.TButton')
generate_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

password_label = ttk.Label(window, text="Сгенерированный пароль:")
password_label.grid(row=2, column=0, padx=5, pady=5)

password_entry = ttk.Entry(window)
password_entry.grid(row=2, column=1, padx=5, pady=5)

style = ttk.Style()
style.configure('my.TButton', font=('Arial', 12),
                background='#4CAF50', foreground='white', borderwidth=0)
style.map('my.TButton', background=[
          ('active', '#009900'), ('!disabled', '#990000')])
style.configure('my.TButton', foreground='black')
style.configure('my.TButton', padding=10, border_radius=40)
window.mainloop()
