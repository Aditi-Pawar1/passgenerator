import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip             

def generate_password():
    length = length_var.get()
    use_lower = use_lowercase.get()
    use_upper = use_uppercase.get()
    use_digit = use_digits.get()
    use_symbol = use_symbols.get()
    
    characters = ''
    
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digit:
        characters += string.digits
    if use_symbol:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
  
    use_lowercase.set(False)
    use_uppercase.set(False)
    use_digits.set(False)
    use_symbols.set(False)


root = tk.Tk()
root.title("Password Generator")


window_size = 500  
window_width = window_size
window_height = window_size

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

mainframe = ttk.Frame(root, padding="20")
mainframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 10))
style.configure('TButton', font=('Helvetica', 10))


style.configure('TButton', padding=20, width=30)

length_label = ttk.Label(mainframe, text="Password Length:")
length_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

length_var = tk.IntVar()
length_entry = ttk.Entry(mainframe, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)
length_entry.insert(0, 12)

use_lowercase = tk.BooleanVar()
lowercase_check = ttk.Checkbutton(mainframe, text="Lowercase", variable=use_lowercase)
lowercase_check.grid(row=1, column=0, sticky=tk.W, padx=50, pady=20)

use_uppercase = tk.BooleanVar()
uppercase_check = ttk.Checkbutton(mainframe, text="Uppercase", variable=use_uppercase)
uppercase_check.grid(row=2, column=0, sticky=tk.W, padx=50, pady=20)

use_digits = tk.BooleanVar()
digits_check = ttk.Checkbutton(mainframe, text="Digits", variable=use_digits)
digits_check.grid(row=3, column=0, sticky=tk.W, padx=50, pady=20)

use_symbols = tk.BooleanVar()
symbols_check = ttk.Checkbutton(mainframe, text="Symbols", variable=use_symbols)
symbols_check.grid(row=4, column=0, sticky=tk.W, padx=50, pady=20)

generate_button = ttk.Button(mainframe, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=20)

password_label = ttk.Label(mainframe, text="Generated Password:")
password_label.grid(row=6, column=0, sticky=tk.W, padx=10, pady=10)

password_entry = ttk.Entry(mainframe, width=40)
password_entry.grid(row=6, column=1, sticky=tk.W, padx=10, pady=10)


root.mainloop()

   



  
