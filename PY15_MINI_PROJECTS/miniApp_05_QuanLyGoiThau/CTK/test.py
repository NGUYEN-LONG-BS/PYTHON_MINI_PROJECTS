import os
import sys
from customtkinter import *
from PIL import Image
from datetime import datetime
import json

# ======================================================================================
# CREATE USER FORM
# ======================================================================================
app = CTk()
app.geometry("900x800")
# Create the main application window
app.title("QUẢN LÝ GÓI THẦU")

def write_settings(mode, theme):
    settings = {
    "appearance_mode": mode,
    "color_theme": theme
    }
    with open("json/setup.txt", "w") as file:
        json.dump(settings, file)

def refresh_form():
    for widget in app.winfo_children():
        widget.destroy()
        create_widgets()
# ======================================================================================
# SWITCH FOR DARK/LIGHT MODE
# ======================================================================================
def switch_mode():
    current_mode = get_appearance_mode()
    if current_mode == "Light":
        set_appearance_mode("dark")
        write_settings("dark", combobox.get())
    else:
        set_appearance_mode("light")
        write_settings("light", combobox.get())
refresh_form()  # Refresh the form

# ======================================================================================
# COMBOBOX FOR COLOR THEME
# ======================================================================================
def change_theme(choice):
    theme_path = f"json/{choice}.json"
    if os.path.exists(theme_path):
        set_default_color_theme(theme_path)
        write_settings(get_appearance_mode(), choice)
        refresh_form()  # Refresh the form
    else:
        print(f"Theme file {theme_path} not found.")

def create_widgets():
    global switch, combobox, LABEL_NamGoiThau

switch = CTkSwitch(master=app, text="Dark Mode", command=switch_mode)
switch.place(x=50, y=20)

themes = ["MoonlitSky", "NeonBanana", "DaynNight"]
combobox = CTkComboBox(master=app, values=themes, command=change_theme)
combobox.place(x=200, y=20)

LABEL_NamGoiThau = CTkLabel(master=app, text="Năm gói thầu", font=("", 18))
LABEL_NamGoiThau.place(x=50, y=70)

create_widgets()

# ======================================================================================
# MAINLOOP
# ======================================================================================
app.mainloop()