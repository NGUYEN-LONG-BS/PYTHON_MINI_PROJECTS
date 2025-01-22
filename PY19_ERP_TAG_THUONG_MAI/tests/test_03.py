import tkinter as tk
from tkinter import ttk

class RealTimeHighlightTreeview(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Real-Time Highlight Treeview")
        self.geometry("400x300")

        # Tạo Treeview
        self.tree = ttk.Treeview(self, columns=("Name", "Age"), show="headings", height=10)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Định nghĩa cột
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.column("Name", width=200)
        self.tree.column("Age", width=100)

        # Thêm dữ liệu mẫu
        for i, (name, age) in enumerate([("Alice", 25), ("Bob", 30), ("Charlie", 22), ("Diana", 28)]):
            self.tree.insert("", "end", iid=i, values=(name, age))

        # Biến để theo dõi dòng được highlight
        self.current_highlighted = None

        # Gắn sự kiện <<TreeviewMotion>>
        self.tree.bind("<<TreeviewMotion>>", self.highlight_row)

    def highlight_row(self, event):
        # Lấy ID của dòng dưới con trỏ chuột
        row_id = self.tree.identify_row(event.y)

        # Bỏ highlight dòng trước đó (nếu có)
        if self.current_highlighted and self.current_highlighted != row_id:
            self.tree.item(self.current_highlighted, tags=())

        # Highlight dòng mới
        if row_id and row_id != self.current_highlighted:
            self.tree.item(row_id, tags=("highlighted",))
            self.tree.tag_configure("highlighted", background="lightblue")
            self.current_highlighted = row_id


if __name__ == "__main__":
    app = RealTimeHighlightTreeview()
    app.mainloop()
