"""
    Lấy dữ liệu về và hiển thị lên form LOCAL SQL
    
"""
import pyodbc
import customtkinter as ctk


def fetch_data():
    try:
        # Connection details
        server = 'KSNB3\\SQLEXPRESS'  # Replace with your server name
        database = 'DATABASE_USER_ID'  # Replace with your database name
        username = 'sa'  # Replace with your SQL Server username
        password = 'Ta#9999'  # Replace with your password
        
        # server = '103.90.227.154'  # Replace with your server name
        # database = 'LA_2024'  # Replace with your database name
        # username = 'sa'  # Replace with your SQL Server username
        # password = 'Ta#9999'  # Replace with your password

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
        cursor.execute('SELECT * FROM TB_DS_DATABASE')  # Replace with your table
        # cursor.execute('SELECT * FROM [LA_2024].[dbo].[TB_COMPONENT_CATEGORIES]')
        rows = cursor.fetchall()

        # Close connections
        cursor.close()
        conn.close()

        return rows

    except pyodbc.Error as e:
        print(f"Database connection error: {e}")
        return None


def display_data(data):
    if not data:
        print("No data to display.")
        return

    # Create the main window
    root = ctk.CTk()
    root.title("SQL Server Data Viewer")
    root.geometry("800x600")

    # Create a tab view
    tabview = ctk.CTkTabview(root, width=780, height=580)
    tabview.pack(padx=10, pady=10)

    # Add a tab for the data table
    data_tab = tabview.add("Data Table")

    # Create a frame for the data
    frame = ctk.CTkFrame(data_tab)
    frame.pack(padx=10, pady=10)

    # Create a table (using a simple grid layout)
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            label = ctk.CTkLabel(frame, text=value, anchor="w", width=15)
            label.grid(row=i, column=j, padx=5, pady=5)

    # Add an Info tab for additional content
    info_tab = tabview.add("Info")
    info_label = ctk.CTkLabel(info_tab, text="This tab can display additional information.")
    info_label.pack(padx=20, pady=20)

    # Run the main loop
    root.mainloop()


if __name__ == "__main__":
    # Fetch data from SQL Server
    data = fetch_data()
    display_data(data)
