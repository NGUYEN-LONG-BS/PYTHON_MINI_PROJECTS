import os
from customtkinter import set_default_color_theme

def load_theme(theme_name):
    theme_path = f"json/{theme_name}.json"
    if os.path.exists(theme_path):
        set_default_color_theme(theme_path)
        print(f"Loaded theme: {theme_path}")
    else:
        print(f"Theme not found: {theme_path}")
