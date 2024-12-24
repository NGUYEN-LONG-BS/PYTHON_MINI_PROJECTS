import tkinter as tk
from tkinter import ttk

def submit_form():
    # Get form data
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get("1.0", "end-1c")

    # Save data (e.g., database, file)
    print("Customer registered successfully!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Address: {address}")

root = tk.Tk()
root.title("New Customer Registration")

# Create form fields
form_fields = ttk.Frame(root, padding="20")
form_fields.pack(fill="both", expand=True)

tk.Label(form_fields, text="New Customer Registration", font=("Arial", 18)).grid(column=0, row=0, columnspan=2)

tk.Label(form_fields, text="Name:", font=("Arial", 12)).grid(column=0, row=1)
name_entry = tk.Entry(form_fields, font=("Arial", 12), width=30)
name_entry.grid(column=1, row=1)

tk.Label(form_fields, text="Email:", font=("Arial", 12)).grid(column=0, row=2)
email_entry = tk.Entry(form_fields, font=("Arial", 12), width=30)
email_entry.grid(column=1, row=2)

tk.Label(form_fields, text="Phone:", font=("Arial", 12)).grid(column=0, row=3)
phone_entry = tk.Entry(form_fields, font=("Arial", 12), width=30)
phone_entry.grid(column=1, row=3)

tk.Label(form_fields, text="Address:", font=("Arial", 12)).grid(column=0, row=4)
address_entry = tk.Text(form_fields, font=("Arial", 12), height=5, width=30)
address_entry.grid(column=1, row=4)

submit_button = tk.Button(form_fields, text="Register", command=submit_form, bg="#007bff", fg="white", font=("Arial", 12))
submit_button.grid(column=1, row=5, pady=10)

root.mainloop()