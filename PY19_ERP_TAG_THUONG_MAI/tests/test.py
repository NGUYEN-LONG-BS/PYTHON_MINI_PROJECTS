import tkinter as tk
from tkinter import ttk

class ModernDashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Dashboard")
        self.root.geometry("900x600")
        self.root.configure(bg="#2c3e50")

        self.create_header()
        self.create_tabs()

    def create_header(self):
        header = tk.Frame(self.root, bg="#34495e", height=60)
        header.pack(fill="x")

        title = tk.Label(header, text="Modern Dashboard", font=("Arial", 20, "bold"), bg="#34495e", fg="white")
        title.pack(side="left", padx=20)

    def create_tabs(self):
        # Create a Notebook widget with styled tabs
        style = ttk.Style()
        style.configure("TNotebook", background="#2c3e50", tabmargins=[2, 5, 2, 0])
        style.configure("TNotebook.Tab", background="#34495e", foreground="white", font=("Arial", 12, "bold"))
        style.map("TNotebook.Tab", background=[("selected", "#1abc9c")], foreground=[("selected", "white")])

        self.notebook = ttk.Notebook(self.root, style="TNotebook")
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Create tabs
        self.tab1 = ttk.Frame(self.notebook, style="TFrame")
        self.tab2 = ttk.Frame(self.notebook, style="TFrame")
        self.tab3 = ttk.Frame(self.notebook, style="TFrame")

        # Add tabs to the notebook
        self.notebook.add(self.tab1, text="Dashboard")
        self.notebook.add(self.tab2, text="Settings")
        self.notebook.add(self.tab3, text="About")

        # Add content to each tab
        self.create_dashboard_tab()
        self.create_settings_tab()
        self.create_about_tab()

    def create_dashboard_tab(self):
        label = tk.Label(self.tab1, text="Welcome to the Dashboard", font=("Arial", 18, "bold"), fg="#1abc9c", bg="#2c3e50")
        label.pack(pady=20)

        tk.Button(self.tab1, text="View Reports", font=("Arial", 14), bg="#1abc9c", fg="white", relief="flat", command=self.view_reports).pack(pady=10)

    def create_settings_tab(self):
        label = tk.Label(self.tab2, text="Settings", font=("Arial", 18, "bold"), fg="#1abc9c", bg="#2c3e50")
        label.pack(pady=20)

        tk.Label(self.tab2, text="Option 1:", font=("Arial", 14), fg="white", bg="#2c3e50").pack(anchor="w", padx=20)
        tk.Entry(self.tab2).pack(anchor="w", padx=20, pady=5)

        tk.Label(self.tab2, text="Option 2:", font=("Arial", 14), fg="white", bg="#2c3e50").pack(anchor="w", padx=20)
        tk.Entry(self.tab2).pack(anchor="w", padx=20, pady=5)

        tk.Button(self.tab2, text="Save Settings", font=("Arial", 14), bg="#1abc9c", fg="white", relief="flat", command=self.save_settings).pack(pady=20)

    def create_about_tab(self):
        label = tk.Label(self.tab3, text="About This App", font=("Arial", 18, "bold"), fg="#1abc9c", bg="#2c3e50")
        label.pack(pady=20)

        about_text = "This is a modern dashboard application built with Tkinter.\nIt demonstrates how to create a beautiful and functional UI."
        tk.Label(self.tab3, text=about_text, font=("Arial", 14), fg="white", bg="#2c3e50", wraplength=600, justify="center").pack(pady=10)

    def view_reports(self):
        print("Viewing reports...")

    def save_settings(self):
        print("Settings saved!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernDashboardApp(root)
    root.mainloop()
