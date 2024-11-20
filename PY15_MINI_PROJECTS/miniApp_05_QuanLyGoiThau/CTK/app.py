import os
import sys
from customtkinter import *
from PIL import Image

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the current working directory to the script's directory
os.chdir(script_dir)

app = CTk()
app.geometry("900x800")

# set_appearance_mode("dark")
set_appearance_mode("light")

# ========================================= BUTTON
def click_handler():
    print("Button Clicked")

img = Image.open(r"img\icons8-chat-message-50.png")

btn = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#4158D0",
                hover_color="#C850C0", border_color="#FFCC70",
                border_width=2, image=CTkImage(dark_image=img, light_image=img),
                command=click_handler)
btn.place(relx=0.25, rely=0.1, anchor="center")


app.mainloop()