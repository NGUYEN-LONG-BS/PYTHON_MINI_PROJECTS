# https://www.youtube.com/watch?v=Miydkti_QVE
from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x400")

set_appearance_mode("dark")
# set_appearance_mode("light")

# ========================================= BUTTON
img = Image.open(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY15_MINI_PROJECTS\03.CustomizeTkinter\icons8-chat-message-50.png")

btn = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#4158D0",
                hover_color="#C850C0", border_color="#FFCC70",
                border_width=2, image=CTkImage(dark_image=img, light_image=img))
btn.place(relx=0.5, rely=0.1, anchor="center")

# ========================================= TEXT
label = CTkLabel(master=app, text="Some text", font=("Arial", 20), text_color="#FFCC70")
label.place(relx=0.5, rely=0.2, anchor="center")

# ========================================= COMBOBOX
combobox = CTkComboBox(master=app, values=["option 1","option 2","option 3"], fg_color="#0093E9",
                       border_color="#FBAB7E", dropdown_fg_color="#0093E9")
combobox.place(relx=0.5, rely=0.3, anchor="center")

# ========================================= CHECKBOX
CHECKBOX = CTkCheckBox(master=app, text="Option", fg_color="#C850C0", checkbox_height=30,
                       checkbox_width=30, corner_radius=36)
CHECKBOX.place(relx=0.5, rely=0.4, anchor="center")

# ========================================= SWITCH
SWITCH = CTkSwitch(master=app, text="Option")
SWITCH.place(relx=0.5, rely=0.5, anchor="center")

# ========================================= SLIDER
app.mainloop()