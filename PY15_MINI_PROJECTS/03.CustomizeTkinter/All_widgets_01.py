# https://www.youtube.com/watch?v=Miydkti_QVE
from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("900x800")

set_appearance_mode("dark")
# set_appearance_mode("light")

# ========================================= BUTTON
def click_handler():
    print("Button Clicked")

img = Image.open(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY15_MINI_PROJECTS\03.CustomizeTkinter\icons8-chat-message-50.png")

btn = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#4158D0",
                hover_color="#C850C0", border_color="#FFCC70",
                border_width=2, image=CTkImage(dark_image=img, light_image=img),
                command=click_handler)
btn.place(relx=0.25, rely=0.1, anchor="center")

# ========================================= LABEL
label = CTkLabel(master=app, text="Some text", font=("Arial", 20), text_color="#FFCC70")
label.place(relx=0.25, rely=0.2, anchor="center")

# ========================================= COMBOBOX
def change_handler(value):
    print(f"Selected Value {value}")

combobox = CTkComboBox(master=app, values=["option 1","option 2","option 3"], fg_color="#0093E9",
                       border_color="#FBAB7E", dropdown_fg_color="#0093E9",
                       command=change_handler)
combobox.place(relx=0.25, rely=0.3, anchor="center")

# ========================================= CHECKBOX
CHECKBOX = CTkCheckBox(master=app, text="Option", fg_color="#C850C0", checkbox_height=30,
                       checkbox_width=30, corner_radius=36)
CHECKBOX.place(relx=0.25, rely=0.4, anchor="center")

# ========================================= SWITCH
SWITCH = CTkSwitch(master=app, text="Option")
SWITCH.place(relx=0.25, rely=0.5, anchor="center")

# ========================================= SLIDER
SLIDER = CTkSlider(master=app, from_=0, to=100, number_of_steps=5,
                   button_color="#C850C0", progress_color="#C850C0",
                   orientation="vertical")
SLIDER.place(relx=0.5, rely=0.2, anchor="center")

# ========================================= ENTRY
entry = CTkEntry(master=app, placeholder_text="Start typing...", width=300,
                 text_color="#FFCC70")
entry.place(relx=0.25, rely=0.6, anchor="center")

# ========================================= TEXTBOX
textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70",
                     scrollbar_button_hover_color="#FF9970", corner_radius=16,
                     border_color="#FFCC70", border_width=2, width=200, height=100)
textbox.place(x=550, y=100)

# ========================================= GET ENTERED VALUE WITH ENTRY
def click_handler_with_entry():
    print(f"Entered Value: {entry_with_BTN.get()}")
    
entry_with_BTN = CTkEntry(master=app, placeholder_text="Start typing...", width=300,
                 text_color="#FFCC70")
entry_with_BTN.place(relx=0.25, rely=0.7, anchor="center")

btn_WITH_ENTRY = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#4158D0",
                hover_color="#C850C0", border_color="#FFCC70",
                border_width=2, image=CTkImage(dark_image=img, light_image=img),
                command=click_handler_with_entry,
                width=300)
btn_WITH_ENTRY.place(relx=0.25, rely=0.75, anchor="center")

# ========================================= GET ENTERED VALUE WITH TEXTBOX
def click_handler_with_textbox():
    print(f"Entered Value: {textbox_WITH_BTN.get('0.0','end')}")
    
textbox_WITH_BTN = CTkTextbox(master=app, scrollbar_button_color="#FFCC70",
                     scrollbar_button_hover_color="#FF9970", corner_radius=16,
                     border_color="#FFCC70", border_width=2, width=200, height=100)
textbox_WITH_BTN.place(x=550, y=250)

btn_WITH_TEXTBOX = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#4158D0",
                hover_color="#C850C0", border_color="#FFCC70",
                border_width=2, image=CTkImage(dark_image=img, light_image=img),
                command=click_handler_with_textbox,
                width=200)
btn_WITH_TEXTBOX.place(x=550, y=360)

# ========================================= Update the label's text
count = 0
def click_handler_with_label():
    global count
    count += 1
    label_with_BTN.configure(text=f"You've clicked the button {count} times")
    
label_with_BTN = CTkLabel(master=app, text="Some text", font=("Arial", 20), text_color="#FFCC70")
label_with_BTN.place(x=550, y=450)

btn_WITH_label = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#4158D0",
                hover_color="#C850C0", border_color="#FFCC70",
                border_width=2, image=CTkImage(dark_image=img, light_image=img),
                command=click_handler_with_label,
                width=200)
btn_WITH_label.place(x=550, y=480)

app.mainloop()