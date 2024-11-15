import smtplib
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender_email = sender_entry.get()
    sender_password = password_entry.get()
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    if not (sender_email and sender_password and recipient_email and subject and body.strip()):
        messagebox.showwarning("Warning", "All fields must be filled!")
        return

    try:
        # Set up the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, recipient_email, message)
            messagebox.showinfo("Success", "Email sent successfully!")
            clear_fields()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

def clear_fields():
    sender_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    recipient_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    body_text.delete("1.0", tk.END)

# GUI setup
window = tk.Tk()
window.title("Email Sender")
window.geometry("400x400")

# Labels and input fields
tk.Label(window, text="Sender Email:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
sender_entry = tk.Entry(window, width=40)
sender_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
password_entry = tk.Entry(window, show="*", width=40)
password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Recipient Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
recipient_entry = tk.Entry(window, width=40)
recipient_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Subject:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
subject_entry = tk.Entry(window, width=40)
subject_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(window, text="Body:").grid(row=4, column=0, padx=10, pady=5, sticky="nw")
body_text = tk.Text(window, width=30, height=10)
body_text.grid(row=4, column=1, padx=10, pady=5)

# Buttons
send_button = tk.Button(window, text="Send Email", command=send_email, bg="green", fg="white")
send_button.grid(row=5, column=0, columnspan=2, pady=10)

clear_button = tk.Button(window, text="Clear Fields", command=clear_fields, bg="red", fg="white")
clear_button.grid(row=6, column=0, columnspan=2, pady=5)

# Run the GUI
window.mainloop()
