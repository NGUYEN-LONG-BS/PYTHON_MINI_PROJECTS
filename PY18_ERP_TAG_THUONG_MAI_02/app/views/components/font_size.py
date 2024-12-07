# Project/views/components/font_size.py
import tkinter as tk
from tkinter import font

# Reusable function to set font for menu items
def set_menu_font(menu, size=15):
    """Set the font for menu items to a specified size."""
    custom_font = font.Font(family="TkDefaultFont", size=size)  # Create a new Font object with the desired size
    menu.config(font=custom_font)  # Apply the font to the menu


