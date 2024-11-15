import tkinter as tk
from tkinter import ttk, messagebox


class BloggingPlatform:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Blogging Platform")
        self.root.geometry("800x600")

        # Style configuration
        style = ttk.Style()
        style.theme_use("clam")  # Using 'clam' theme for a modern look
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("Treeview", font=("Arial", 10))

        # Blog posts storage
        self.posts = []

        # Input frame
        input_frame = ttk.Frame(root, padding="10")
        input_frame.pack(fill="x")

        ttk.Label(input_frame, text="Title:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.title_entry = ttk.Entry(input_frame, width=50)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Content:", font=("Arial", 12)).grid(row=1, column=0, sticky="nw", padx=5, pady=5)
        self.content_text = tk.Text(input_frame, width=50, height=5, font=("Arial", 10))
        self.content_text.grid(row=1, column=1, padx=5, pady=5)

        # Buttons frame
        buttons_frame = ttk.Frame(root, padding="10")
        buttons_frame.pack(fill="x")

        ttk.Button(buttons_frame, text="Add Post", command=self.add_post).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Delete Selected Post", command=self.delete_post).grid(row=0, column=1, padx=5, pady=5)

        # Posts table frame
        table_frame = ttk.Frame(root, padding="10")
        table_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(table_frame, columns=("Title", "Content"), show="headings", height=10)
        self.tree.pack(fill="both", expand=True)

        self.tree.heading("Title", text="Title")
        self.tree.heading("Content", text="Content")
        self.tree.column("Title", width=200, anchor="w")
        self.tree.column("Content", width=500, anchor="w")

        # Scrollbar for the table
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def add_post(self):
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not title or not content:
            messagebox.showwarning("Warning", "Both Title and Content are required!")
            return

        self.posts.append({"title": title, "content": content})
        self.update_table()
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)

    def delete_post(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No post selected!")
            return

        index = int(selected_item[0][1:]) - 1  # Extract index from Treeview item ID
        del self.posts[index]
        self.update_table()

    def update_table(self):
        # Clear the table
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Populate table
        for idx, post in enumerate(self.posts):
            self.tree.insert("", "end", iid=f"I{idx+1}", values=(post["title"], post["content"][:50] + "..."))


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BloggingPlatform(root)
    root.mainloop()
