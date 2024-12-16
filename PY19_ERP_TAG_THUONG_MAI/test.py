import tkinter as tk

def on_option1():
    print("Option 1 selected")

def on_option2():
    print("Option 2 selected")

def on_suboption1():
    print("Suboption 1 selected")

def on_suboption2():
    print("Suboption 2 selected")

def on_subsuboption1():
    print("Subsuboption 1 selected")

def on_subsuboption2():
    print("Subsuboption 2 selected")

# Create the main window
root = tk.Tk()
root.title("3-Level Menu Example")

# Create the top-level menu
menu_bar = tk.Menu(root)

# Create the first level of the menu (File)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add options to the File menu
file_menu.add_command(label="Option 1", command=on_option1)
file_menu.add_command(label="Option 2", command=on_option2)

# Create the second level of the menu (Edit)
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Create the third level (Submenu under Edit)
submenu = tk.Menu(edit_menu, tearoff=0)
edit_menu.add_cascade(label="Submenu", menu=submenu)

# Add suboptions to the submenu
submenu.add_command(label="Suboption 1", command=on_suboption1)
submenu.add_command(label="Suboption 2", command=on_suboption2)

# Create the fourth level (Subsubmenu under Submenu)
subsubmenu = tk.Menu(submenu, tearoff=0)
submenu.add_cascade(label="Subsubmenu", menu=subsubmenu)

# Add subsuboptions to the subsubmenu
subsubmenu.add_command(label="Subsuboption 1", command=on_subsuboption1)
subsubmenu.add_command(label="Subsuboption 2", command=on_subsuboption2)

# Display the menu
root.config(menu=menu_bar)

# Start the Tkinter event loop
root.mainloop()
