#making a calculator gui with number buttons and operator buttons using tkinter

import tkinter as tk
from tkinter import ttk

def click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget to display calculations
entry = ttk.Entry(root, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10,)

# Button labels
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

# Create buttons and add to the grid
print(dict(enumerate(buttons, 1)))

for r, row in enumerate(buttons, 1):
    for c, btn_text in enumerate(row):
        btn = ttk.Button(root, text=btn_text, command=lambda b=btn_text: click(b))
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# Adjust row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the application
root.mainloop()
