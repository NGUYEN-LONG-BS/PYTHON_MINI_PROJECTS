# https://www.youtube.com/watch?v=Miydkti_QVE
from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("900x800")

set_appearance_mode("dark")
# set_appearance_mode("light")

# ========================================= FRAMES no scroll
frame_01 = CTkFrame(master=app, fg_color="#8D6F3A", border_color="#FFCC70",
                    border_width=2)
# frame_01.pack(expand=True)
frame_01.place(relx=0.25, rely=0.1, anchor="center")

label_01 = CTkLabel(master=frame_01, text="This is a frame_01")
entry_01 = CTkEntry(master=frame_01, placeholder_text="Type something...")
btn_01 = CTkButton(master=frame_01, text="Submit")

label_01.pack(anchor='s', expand=True, pady=10, padx=30)
entry_01.pack(anchor='s', expand=True, pady=10, padx=30)
btn_01.pack(anchor='n', expand=True, pady=10, padx=30)

# ========================================= FRAMES with scroll
frame_02 = CTkScrollableFrame(master=app, fg_color="#8D6F3A", border_color="#FFCC70",
                    border_width=2, orientation="vertical", scrollbar_button_color="#FFCC70",
                    scrollbar_button_hover_color="#FF9970")
# frame_01.pack(expand=True)
frame_02.place(relx=0.25, rely=0.4, anchor="center")

label_02 = CTkLabel(master=frame_02, text="This is a frame_02")
entry_02 = CTkEntry(master=frame_02, placeholder_text="Type something...")
btn_02 = CTkButton(master=frame_02, text="Submit")

label_02.pack(anchor='s', expand=True, pady=10, padx=30)
entry_02.pack(anchor='s', expand=True, pady=10, padx=30)
btn_02.pack(anchor='n', expand=True, pady=10, padx=30)
CTkButton(master=frame_02, text="Another Widget").pack(expand=TRUE, padx=30, pady=20)
CTkButton(master=frame_02, text="Another Widget").pack(expand=TRUE, padx=30, pady=20)
CTkButton(master=frame_02, text="Another Widget").pack(expand=TRUE, padx=30, pady=20)
CTkButton(master=frame_02, text="Another Widget").pack(expand=TRUE, padx=30, pady=20)
CTkButton(master=frame_02, text="Another Widget").pack(expand=TRUE, padx=30, pady=20)

# ========================================= Tab tree
tabview_01 = CTkTabview(master=app)
# tabview_01.pack(padx=20,pady=20)
# tabview_01.place(x=500, y=400)
tabview_01.place(relx=0.25, rely=0.75, anchor="center")

tabview_01.add("Tab 1")
tabview_01.add("Tab 2")
tabview_01.add("Tab 3")


label_01 = CTkLabel(master=tabview_01.tab("Tab 1"), text="This is tab 01")
label_01.pack(padx=20, pady=20)

label_02 = CTkLabel(master=tabview_01.tab("Tab 2"), text="This is tab 02")
label_02.pack(padx=20, pady=20)

label_03 = CTkLabel(master=tabview_01.tab("Tab 3"), text="This is tab 03")
label_03.pack(padx=20, pady=20)

# ========================================= Change color quickly
# https://github.com/avalon60/ctk_theme_builder/tree/develop/user_themes
# set_default_color_theme("blue")         # change color
# set_default_color_theme("green")        # change color
# set_default_color_theme("dark-blue")        # change color
set_default_color_theme(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY15_MINI_PROJECTS\03.CustomizeTkinter\MoonlitSky.json")        # change color
# set_default_color_theme(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY15_MINI_PROJECTS\03.CustomizeTkinter\DaynNight.json")        # change color
# set_default_color_theme(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY15_MINI_PROJECTS\03.CustomizeTkinter\NeonBanana.json")        # change color


frame_03 = CTkFrame(master=app, border_color="#FFCC70", border_width=2)
frame_03.place(relx=0.5, rely=0.1)
CTkButton(master=frame_03, text="Button"). pack (pady=20, padx=20)
CTkCheckBox(master=frame_03, text="Check box"). pack (pady=20, padx=20)
CTkComboBox(master=frame_03, values=["Option 1", "Option 2", "Option 3"]).pack (pady=20, padx=20)
CTkEntry(master=frame_03, placeholder_text="Start typing..."). pack (pady=20, padx=20)
CTkProgressBar(master=frame_03). pack (pady=20, padx=20)
CTkRadioButton(master=frame_03, text="Radio button").pack (pady=20, padx=20)
CTkSlider(master=frame_03).pack (pady=20, padx=20)
CTkSwitch(master=frame_03, text="Option"). pack (pady=20, padx=20)

app.mainloop()