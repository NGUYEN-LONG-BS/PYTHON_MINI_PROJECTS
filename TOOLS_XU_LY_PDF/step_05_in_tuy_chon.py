import tkinter as tk
from tkinter import filedialog, messagebox
import win32print
import win32api

class PdfPrinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Printer")

        # Set window size
        self.root.geometry("400x200")

        # Add instructions
        self.label = tk.Label(root, text="Select PDF files to print", font=("Helvetica", 14))
        self.label.pack(pady=20)

        # Button to select files
        self.select_button = tk.Button(root, text="Select PDF Files", command=self.select_files, width=20)
        self.select_button.pack(pady=10)

        # Button to print the selected files
        self.print_button = tk.Button(root, text="Print PDFs", command=self.print_pdfs, width=20, state=tk.DISABLED)
        self.print_button.pack(pady=10)

        # Store the selected files
        self.selected_files = []

    def select_files(self):
        # Let the user select one or multiple PDF files
        self.selected_files = filedialog.askopenfilenames(
            title="Select PDF files", filetypes=[("PDF Files", "*.pdf")]
        )
        
        # Update the print button state
        if self.selected_files:
            self.print_button.config(state=tk.NORMAL)
            messagebox.showinfo("Files Selected", f"{len(self.selected_files)} file(s) selected.")
        else:
            self.print_button.config(state=tk.DISABLED)

    def print_pdfs(self):
        if not self.selected_files:
            messagebox.showerror("Error", "No files selected.")
            return
        
        # Try printing each PDF
        for file_path in self.selected_files:
            self.print_pdf(file_path)
        
        messagebox.showinfo("Printing", "PDFs sent to the printer.")

    def print_pdf(self, file_path):
        try:
            # Get default printer
            printer_name = win32print.GetDefaultPrinter()

            # Send the PDF to the printer
            win32api.ShellExecute(0, "print", file_path, f'/d:"{printer_name}"', ".", 0)
            print(f"Printing {file_path}...")
        except Exception as e:
            print(f"Failed to print {file_path}: {e}")

# Set up the tkinter window
root = tk.Tk()
app = PdfPrinterApp(root)
root.mainloop()
