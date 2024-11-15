import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Create main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget to display numbers and results
entry = tk.Entry(window, width=20, borderwidth=5, font=("Arial", 14), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(window, text=text, width=5, height=2, bg="green", fg="white",
                        command=calculate)
    elif text == "C":
        btn = tk.Button(window, text=text, width=5, height=2, bg="red", fg="white",
                        command=clear_entry)
    else:
        btn = tk.Button(window, text=text, width=5, height=2, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the application
window.mainloop()
