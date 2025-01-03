import pyodbc
import customtkinter as ctk
from tkinter import Canvas, Frame, Scrollbar


def fetch_data():
    try:
        # Connection details
        # server = 'KSNB3\\SQLEXPRESS'  # Replace with your server name
        # database = 'DATABASE_USER_ID'  # Replace with your database name
        # username = 'sa'  # Replace with your SQL Server username
        # password = 'your_password'  # Replace with your password

        server = '103.90.227.154'  # Replace with your server name
        database = 'LA_2024'  # Replace with your database name
        username = 'sa'  # Replace with your SQL Server username
        password = 'Ta#9999'  # Replace with your password

        # SQL Server Authentication
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};PORT=1433'
        )

        # Uncomment this if you want to use Windows Authentication instead:
        # conn = pyodbc.connect(
        #     f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;PORT=1433'
        # )

        # Execute query
        cursor = conn.cursor()
        # cursor.execute('SELECT * FROM TB_DS_DATABASE')  # Replace with your table
        cursor.execute('SELECT * FROM [LA_2024].[dbo].[TB_COMPONENT_CATEGORIES]')
        rows = cursor.fetchall()

        # Close connections
        cursor.close()
        conn.close()

        return rows

    except pyodbc.Error as e:
        print(f"Database connection error: {e}")
        return None


class PaginatedScrollableTableApp:
    def __init__(self, root, data, rows_per_page=20):
        self.root = root
        self.data = data
        self.rows_per_page = rows_per_page
        self.current_page = 0

        self.root.title("Scrollable Paginated SQL Server Data Viewer")
        self.root.geometry("800x600")

        # Create main frame
        self.main_frame = ctk.CTkFrame(root)
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Create a scrollable table
        self.scrollable_frame = self.create_scrollable_frame()

        # Create navigation buttons
        self.nav_frame = ctk.CTkFrame(self.main_frame)
        self.nav_frame.pack()

        self.prev_button = ctk.CTkButton(self.nav_frame, text="Previous", command=self.prev_page)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.page_label = ctk.CTkLabel(self.nav_frame, text=f"Page {self.current_page + 1}")
        self.page_label.grid(row=0, column=1, padx=5)

        self.next_button = ctk.CTkButton(self.nav_frame, text="Next", command=self.next_page)
        self.next_button.grid(row=0, column=2, padx=5)

        # Render the first page
        self.render_page()

    def create_scrollable_frame(self):
        """
        Create a scrollable frame for the table.
        """
        # Create a canvas
        canvas = Canvas(self.main_frame, width=760, height=450, bg="white")
        canvas.pack(side="left", fill="both", expand=True)

        # Add a vertical scrollbar
        scrollbar = Scrollbar(self.main_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas
        frame = Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        return frame

    def render_page(self):
        """
        Render the current page's data in the scrollable frame.
        """
        # Clear the current table
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Calculate the range of rows for the current page
        start_index = self.current_page * self.rows_per_page
        end_index = start_index + self.rows_per_page
        page_data = self.data[start_index:end_index]

        # Populate the table with the current page's data
        for i, row in enumerate(page_data):
            for j, value in enumerate(row):
                label = ctk.CTkLabel(self.scrollable_frame, text=value, anchor="w", width=15)
                label.grid(row=i, column=j, padx=5, pady=5)

        # Update the page label
        self.page_label.configure(text=f"Page {self.current_page + 1}")

        # Enable/disable navigation buttons as needed
        self.prev_button.configure(state="normal" if self.current_page > 0 else "disabled")
        self.next_button.configure(state="normal" if end_index < len(self.data) else "disabled")

    def next_page(self):
        if (self.current_page + 1) * self.rows_per_page < len(self.data):
            self.current_page += 1
            self.render_page()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.render_page()


if __name__ == "__main__":
    # Fetch data from SQL Server
    data = fetch_data()

    if data:
        root = ctk.CTk()
        app = PaginatedScrollableTableApp(root, data, rows_per_page=20)  # Show 20 rows per page
        root.mainloop()
    else:
        print("No data available.")
