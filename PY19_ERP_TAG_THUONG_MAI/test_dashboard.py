import tkinter as tk
from tkinter import ttk

# Create the main app window
root = tk.Tk()
root.title("Tkinter Dashboard")
root.geometry("1000x600")
root.configure(bg="#2C3E50")

# Header
header = tk.Frame(root, bg="#1ABC9C", height=60)
header.pack(fill="x")

header_label = tk.Label(header, text="Dashboard", font=("Arial", 24, "bold"), bg="#1ABC9C", fg="white")
header_label.pack(pady=10)

# Sidebar
sidebar = tk.Frame(root, bg="#34495E", width=200)
sidebar.pack(side="left", fill="y")

# Sidebar buttons
sidebar_buttons = ["Overview", "Reports", "Settings", "Help"]
for btn in sidebar_buttons:
    tk.Button(
        sidebar,
        text=btn,
        font=("Arial", 12),
        bg="#34495E",
        fg="white",
        activebackground="#1ABC9C",
        activeforeground="white",
        bd=0,
        padx=20,
        pady=10
    ).pack(fill="x", pady=5)

# Main Content Area
main_content = tk.Frame(root, bg="white")
main_content.pack(side="right", fill="both", expand=True)

# Tabs for different views
notebook = ttk.Notebook(main_content)
notebook.pack(fill="both", expand=True)

# Tab 1: Overview
overview_tab = ttk.Frame(notebook)
notebook.add(overview_tab, text="Overview")

# Add widgets to the overview tab
overview_label = tk.Label(overview_tab, text="Welcome to the Overview", font=("Arial", 16), bg="white", fg="#2C3E50")
overview_label.pack(pady=20)

stats_frame = tk.Frame(overview_tab, bg="white", pady=20)
stats_frame.pack(fill="x")

# Add simple stats
stat_items = [
    ("Users Online", "125"),
    ("New Signups", "45"),
    ("Total Revenue", "$15,000"),
    ("Tasks Completed", "87%")
]

for title, value in stat_items:
    frame = tk.Frame(stats_frame, bg="white", pady=10, padx=20)
    frame.pack(side="left", fill="y", expand=True)
    tk.Label(frame, text=title, font=("Arial", 12), bg="white", fg="#2C3E50").pack()
    tk.Label(frame, text=value, font=("Arial", 16, "bold"), bg="white", fg="#1ABC9C").pack()

# Tab 2: Reports
reports_tab = ttk.Frame(notebook)
notebook.add(reports_tab, text="Reports")

# Add a sample table to the reports tab
tree = ttk.Treeview(reports_tab, columns=("ID", "Name", "Status"), show="headings")
tree.pack(fill="both", expand=True, padx=10, pady=10)

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Status", text="Status")

# Example data for the table
data = [
    (1, "Project Alpha", "In Progress"),
    (2, "Project Beta", "Completed"),
    (3, "Project Gamma", "Pending"),
    (4, "Project Delta", "In Progress")
]

for row in data:
    tree.insert("", "end", values=row)

# Tab 3: Settings
settings_tab = ttk.Frame(notebook)
notebook.add(settings_tab, text="Settings")

settings_label = tk.Label(settings_tab, text="Settings Page", font=("Arial", 16), bg="white", fg="#2C3E50")
settings_label.pack(pady=20)

# Footer
footer = tk.Frame(root, bg="#34495E", height=30)
footer.pack(fill="x")

footer_label = tk.Label(footer, text="© 2024 My Dashboard", font=("Arial", 10), bg="#34495E", fg="white")
footer_label.pack()

# Run the app
root.mainloop()
