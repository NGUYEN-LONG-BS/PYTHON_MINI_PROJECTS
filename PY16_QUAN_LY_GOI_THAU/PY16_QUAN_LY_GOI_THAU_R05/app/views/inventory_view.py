import customtkinter as ctk

class InventoryView:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")

    def create_widgets(self):
        label = ctk.CTkLabel(self.root, text="Inventory Module")
        label.pack(pady=10)

        add_button = ctk.CTkButton(self.root, text="Add Item", command=self.add_item)
        add_button.pack(pady=5)

    def add_item(self):
        print("Add Item logic here")

    def run(self):
        self.create_widgets()
        self.root.mainloop()
