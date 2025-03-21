import os
import ast
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import defaultdict

def scan_imports(directory):
    """Scan a directory for Python files and extract imported modules."""
    imports = defaultdict(set)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read(), filename=file)
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                for alias in node.names:
                                    imports[alias.name].add(None)  # None means no specific version
                            elif isinstance(node, ast.ImportFrom):
                                module = node.module
                                for alias in node.names:
                                    imports[module].add(None)
                    except Exception as e:
                        print(f"Error parsing {file}: {e}")

    return imports

def generate_requirements(project_dir, output_file):
    """Generate a requirements.txt file from a project directory."""
    imports = scan_imports(project_dir)
    
    # Filter out None keys and sort the remaining modules
    filtered_modules = [module for module in imports.keys() if module is not None]
    
    with open(output_file, "w", encoding="utf-8") as f:
        for module in sorted(filtered_modules):
            f.write(f"{module}\n")
    
    messagebox.showinfo("Success", f"requirements.txt generated at {output_file}")

def select_project_directory():
    """Open a dialog to select the project directory."""
    directory = filedialog.askdirectory()
    if directory:
        project_dir_var.set(directory)

def select_output_file():
    """Open a dialog to select the output file path."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        output_file_var.set(file_path)

def run_generation():
    """Generate the requirements.txt file."""
    project_dir = project_dir_var.get()
    output_file = output_file_var.get()

    if not project_dir:
        messagebox.showerror("Error", "Please select a project directory.")
        return
    if not output_file:
        messagebox.showerror("Error", "Please select an output file path.")
        return

    generate_requirements(project_dir, output_file)

# Create the main window
root = tk.Tk()
root.title("Generate requirements.txt")

# Variables to store paths
project_dir_var = tk.StringVar()
output_file_var = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Project Directory:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Entry(root, textvariable=project_dir_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_project_directory).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Output File:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Entry(root, textvariable=output_file_var, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_output_file).grid(row=1, column=2, padx=5, pady=5)

tk.Button(root, text="Generate requirements.txt", command=run_generation).grid(row=2, column=1, pady=10)

# Run the application
root.mainloop()