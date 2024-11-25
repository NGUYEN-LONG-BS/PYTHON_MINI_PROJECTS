from app.models.database import Database

class InventoryController:
    def __init__(self, db):
        self.db = db

    def add_item(self, name, quantity, price):
        self.db.query(
            "INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)",
            (name, quantity, price)
        )
        print(f"Item {name} added to inventory.")

    def get_items(self):
        return self.db.query("SELECT * FROM inventory")
