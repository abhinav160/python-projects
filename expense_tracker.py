import tkinter as tk
from tkinter import messagebox, ttk

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        
        # Expense data storage
        self.expenses = []

        # Input fields
        tk.Label(root, text="Description:").grid(row=0, column=0, padx=10, pady=5)
        self.description_entry = tk.Entry(root, width=30)
        self.description_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Amount (₹):").grid(row=1, column=0, padx=10, pady=5)
        self.amount_entry = tk.Entry(root, width=30)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(root, text="Add Expense", command=self.add_expense).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Delete Selected", command=self.delete_expense).grid(row=3, column=0, columnspan=2, pady=10)

        # Table to display expenses
        self.tree = ttk.Treeview(root, columns=("Description", "Amount"), show="headings", height=10)
        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.tree.heading("Description", text="Description")
        self.tree.heading("Amount", text="Amount (₹)")
        
        # Total Label
        self.total_label = tk.Label(root, text="Total: ₹0", font=("Arial", 14))
        self.total_label.grid(row=5, column=0, columnspan=2, pady=10)

    def add_expense(self):
        description = self.description_entry.get()
        amount = self.amount_entry.get()

        if not description or not amount:
            messagebox.showwarning("Warning", "Both fields are required!")
            return

        try:
            amount = float(amount)
            self.expenses.append({"description": description, "amount": amount})
            self.update_table()
            self.description_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a valid number!")

    def delete_expense(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No expense selected!")
            return
        
        index = int(selected_item[0][1:]) - 1  # Get index from Treeview item ID
        del self.expenses[index]
        self.update_table()

    def update_table(self):
        # Clear table
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Refill table
        for idx, expense in enumerate(self.expenses):
            self.tree.insert("", "end", iid=f"I{idx+1}", values=(expense["description"], f"₹{expense['amount']}"))

        # Update total
        total = sum(expense["amount"] for expense in self.expenses)
        self.total_label.config(text=f"Total: ₹{total}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
