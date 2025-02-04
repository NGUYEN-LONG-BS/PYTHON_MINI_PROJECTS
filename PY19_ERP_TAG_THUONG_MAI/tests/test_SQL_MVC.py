import pyodbc
import tkinter as tk
from tkinter import ttk

class SQLModel:
    @staticmethod
    def fetch_data(server_name, database_name, login_name, login_pass, table_name):
        """
        Kết nối đến SQL Server và lấy dữ liệu từ bảng.
        """
        connection_string = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={server_name};"
            f"DATABASE={database_name};"
            f"UID={login_name};"
            f"PWD={login_pass}"
        )
        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            # query = f"SELECT * FROM {table_name}"
            query = f"[Proc_TB_KD02_YEU_CAU_DAT_HANG_FILTER_BY_MANY_ARGUMENTS_250204_110h38]'','',''"
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            return columns, data
        except Exception as e:
            print("Lỗi khi lấy dữ liệu:", e)
            return [], []

class SQLController:
    def __init__(self, view, server_name, database_name, login_name, login_pass, table_name):
        self.view = view
        self.server_name = server_name
        self.database_name = database_name
        self.login_name = login_name
        self.login_pass = login_pass
        self.table_name = table_name
        self.load_data()

    def load_data(self):
        columns, data = SQLModel.fetch_data(
            self.server_name, self.database_name, self.login_name, self.login_pass, self.table_name
        )
        self.view.update_treeview(columns, data)

class SQLView:
    def __init__(self, root):
        self.root = root
        self.root.title("Hiển thị dữ liệu từ SQL Server")
        self.tree = ttk.Treeview(root)
        self.tree.pack(expand=True, fill="both")

    def update_treeview(self, columns, data):
        self.tree['columns'] = columns
        self.tree.heading("#0", text="Index")
        self.tree.column("#0", width=50)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")
        for item in self.tree.get_children():
            self.tree.delete(item)
        for idx, row in enumerate(data):
            self.tree.insert("", "end", text=str(idx+1), values=row)

if __name__ == "__main__":
    root = tk.Tk()
    view = SQLView(root)
    controller = SQLController(
        view,
        server_name="14.225.192.238, 1433",
        database_name="TBD_2024",
        login_name="sa",
        login_pass="Ta#9999",
        table_name="[TB_KD02_YEU_CAU_DAT_HANG]"
    )
    root.mainloop()
