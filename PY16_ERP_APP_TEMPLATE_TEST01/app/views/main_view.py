from customtkinter import *
from PIL import Image
from datetime import datetime
from app.controllers.main_controller import MainController


def create_app():
    app = CTk()
    app.geometry("900x800")
    app.title("QUẢN LÝ GÓI THẦU")

    # Controller for managing app logic
    controller = MainController()

    # Switch for dark/light mode
    def switch_mode():
        current_mode = get_appearance_mode()
        new_mode = "dark" if current_mode == "Light" else "light"
        set_appearance_mode(new_mode)
        controller.save_default_settings(new_mode, "theme_01")

    switch = CTkSwitch(app, text="Dark Mode", command=switch_mode)
    switch.place(x=500, y=700)

    # Combobox for theme selection
    themes = ["MoonlitSky", "NeonBanana", "DaynNight"]
    combobox = CTkComboBox(app, values=themes, command=controller.change_theme)
    combobox.place(x=650, y=700)

    # Button to create a new folder
    def on_create_folder():
        controller.create_folder()
    BTN_TaoThuMucMoi = CTkButton(app, text="Tạo thư mục mới", command=on_create_folder)
    BTN_TaoThuMucMoi.place(x=50, y=700)

    # Scrollable frame for displaying folder contents
    scrollable_frame = CTkScrollableFrame(app, width=800, height=200)
    scrollable_frame.place(x=50, y=300)

    def refresh_scrollable_frame():
        contents = controller.get_directory_contents()
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        for item in contents:
            label = CTkLabel(scrollable_frame, text=item, font=("", 14))
            label.pack(anchor="w")

    refresh_scrollable_frame()

    return app
