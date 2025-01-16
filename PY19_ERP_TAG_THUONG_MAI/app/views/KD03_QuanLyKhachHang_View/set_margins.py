import tkinter as tk
from tkinter import messagebox
from docx import Document
from docx.shared import Cm


def set_default_margins():
    # Create a new Word document
    doc = Document()

    # Set the margins in centimeters
    section = doc.sections[0]
    section.left_margin = Cm(1)
    section.right_margin = Cm(1.5)
    section.top_margin = Cm(1.5)
    section.bottom_margin = Cm(1.5)

    # Save the document
    file_path = "default_margins.docx"
    doc.save(file_path)

    messagebox.showinfo("Success", f"Default margins set and saved to {file_path}")

# Create the Tkinter application
app = tk.Tk()
app.title("Set Default Word Margins")
app.geometry("300x200")

# Add a label
label = tk.Label(app, text="Set Default Word Margins", font=("Arial", 14))
label.pack(pady=20)

# Add a button to set margins
set_margins_button = tk.Button(app, text="Get Margins file", command=set_default_margins, font=("Arial", 12))
set_margins_button.pack(pady=20)

# Run the Tkinter event loop
app.mainloop()
