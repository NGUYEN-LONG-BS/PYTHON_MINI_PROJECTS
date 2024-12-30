import tkinter as tk
from tkinter import ttk
import json


class JsonTreeview:
    def __init__(self, master, json_data=None):
        self.tree = ttk.Treeview(master)

        # Define default data if no JSON is provided
        if json_data is None:
            json_data = {
                "Root": {
                    "Child 1": {
                        "Grandchild 1": {},
                        "Grandchild 2": {}
                    },
                    "Child 2": {}
                }
            }

        # Populate the tree
        self.build_tree(json_data)

    def build_tree(self, json_data, parent=""):
        for key, value in json_data.items():
            # Insert the current item into the tree
            node_id = self.tree.insert(parent, "end", text=key)

            # If the current item has children, recursively add them
            if isinstance(value, dict):
                self.build_tree(value, node_id)

    def pack(self, **kwargs):
        self.tree.pack(**kwargs)


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("JSON Treeview Example")
    root.geometry("400x300")

    # Example JSON input
    json_input = json.dumps({
        "Animals": {
            "Mammals": {
                "Dogs": {},
                "Cats": {}
            },
            "Birds": {
                "Parrots": {},
                "Sparrows": {}
            }
        }
    })

    # Pass JSON data to the treeview
    treeview = JsonTreeview(root, json.loads(json_input))
    treeview.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

