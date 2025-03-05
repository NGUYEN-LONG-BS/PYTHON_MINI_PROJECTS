import tkinter as tk

class PreferencesView:
    def __init__(self, master):
        self.master = master
        self.master.title("Preferences")
        self.master.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.notifications_label = tk.Label(self.master, text="Enable Notifications")
        self.notifications_label.pack()

        self.notifications_checkbox = tk.Checkbutton(self.master, text="Enable", variable=self.notifications_var)
        self.notifications_checkbox.pack()

        self.save_button = tk.Button(self.master, text="Save Preferences", command=self.save_preferences)
        self.save_button.pack()

    def save_preferences(self):
        notifications_enabled = self.notifications_var.get()
        print(f"Notifications enabled: {notifications_enabled}")
