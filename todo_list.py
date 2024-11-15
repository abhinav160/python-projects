import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("To-Do List")

# Entry widget to input tasks
task_entry = tk.Entry(window, width=40, font=("Arial", 14))
task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Buttons
add_button = tk.Button(window, text="Add Task", width=15, command=add_task)
add_button.grid(row=1, column=0, padx=10, pady=5)

delete_button = tk.Button(window, text="Delete Task", width=15, command=delete_task)
delete_button.grid(row=1, column=1, padx=10, pady=5)

clear_button = tk.Button(window, text="Clear All Tasks", width=32, command=clear_tasks)
clear_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(window, width=50, height=15, font=("Arial", 12))
task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
window.mainloop()
