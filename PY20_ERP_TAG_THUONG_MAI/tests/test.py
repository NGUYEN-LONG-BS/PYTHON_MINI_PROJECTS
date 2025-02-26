import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling images

# Function to generate connection string
def get_connection_string():
    return f"{ma_thanh_vien}-{loai_phieu}-{so_phieu}"

# Function to handle the connection
def connect():
    messagebox.showinfo("Connection", f"Connected to: {get_connection_string()}")

# Function to refresh the connection string display
def refresh():
    connection_label.config(text=f"Connect to: {get_connection_string()}")

# Define variables
ma_thanh_vien = "TB"
loai_phieu = "YCDH"
so_phieu = "250003"

# Initialize Tkinter window
root = tk.Tk()
root.title("Connection Interface")
root.geometry("320x200")

# Label to display connection string
connection_label = tk.Label(root, text=f"Connect to: {get_connection_string()}", font=("Arial", 12))
connection_label.pack(pady=10)

# Button to connect
connect_button = tk.Button(root, text="Connect", command=connect, font=("Arial", 12), padx=10, pady=5)
connect_button.pack(pady=5)

# Load 48x48 icon
icon_path = "refresh_icon.png"  # Change this to your image path
icon_image = Image.open(icon_path)
icon_image = icon_image.resize((48, 48))  # Ensure it's 48x48
icon_photo = ImageTk.PhotoImage(icon_image)

# Small Refresh Button with Icon
refresh_button = tk.Button(root, image=icon_photo, command=refresh, borderwidth=0)
refresh_button.pack(pady=5)

# Run the GUI loop
root.mainloop()
