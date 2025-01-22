import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.title("Stylish Notebook")
root.geometry("400x300")

# Create a style object
style = ttk.Style()
style.theme_use("default")  # Use default theme (you can experiment with others)

# Customize the notebook style
style.configure("TNotebook", 
                background="#f0f0f0", 
                borderwidth=0)
style.configure("TNotebook.Tab", 
                background="#ffffff", 
                foreground="#000000", 
                padding=[10, 5],
                font=("Arial", 12, "bold"))
style.map("TNotebook.Tab", 
          background=[("selected", "#4caf50")], 
          foreground=[("selected", "#ffffff")],
          expand=[("selected", [1, 1, 1, 0])])

# Create Notebook
notebook = ttk.Notebook(root)

# Create tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Add tabs
notebook.add(tab1, text="Home")
notebook.add(tab2, text="Settings")
notebook.add(tab3, text="Profile")

# Pack the notebook
notebook.pack(expand=1, fill="both")

# Add content to tabs
tk.Label(tab1, text="Welcome to Home Tab", font=("Arial", 14)).pack(pady=20)
tk.Label(tab2, text="Settings Tab", font=("Arial", 14)).pack(pady=20)
tk.Label(tab3, text="Profile Tab", font=("Arial", 14)).pack(pady=20)

# Run the application
root.mainloop()
