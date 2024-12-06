import tkinter as tk

class SettingsView:
    def __init__(self, master):
        self.master = master
        self.master.title("Settings")
        self.master.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.theme_label = tk.Label(self.master, text="Select Theme")
        self.theme_label.pack()

        self.theme_option = tk.StringVar(value="Light")
        self.theme_menu = tk.OptionMenu(self.master, self.theme_option, "Light", "Dark")
        self.theme_menu.pack()

        self.save_button = tk.Button(self.master, text="Save", command=self.save_settings)
        self.save_button.pack()

    def save_settings(self):
        theme = self.theme_option.get()
        print(f"Theme set to: {theme}")
