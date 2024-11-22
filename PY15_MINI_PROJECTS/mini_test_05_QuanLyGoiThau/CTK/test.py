# Kéo dữ liệu từ SQL_SERVER về CustomTkinter


import pyodbc

def fetch_data():
# Connection details
server = 'KSNB3\\SQLEXPRESS'
database = 'DATABASE_USER_ID'
username = 'sa'
password = 'your_password'  # Replace with your actual password

# Connection string with SQL authentication
conn = pyodbc.connect(
f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};PORT=1433'
)

# Create a cursor and execute a query
cursor = conn.cursor()
cursor.execute('SELECT * FROM TB_DS_DATABASE')
rows = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

return rows

Step 2: Display Data in CustomTkinter
import customtkinter as ctk
import tkinter as tk

def display_data(data):
# Create the main window
root = ctk.CTk()
root.title("SQL Server Data")

# Create a frame for the table
frame = ctk.CTkFrame(root)
frame.pack(padx=10, pady=10)

# Create a table (using a simple grid layout)
for i, row in enumerate(data):
for j, value in enumerate(row):
label = ctk.CTkLabel(frame, text=value)
label.grid(row=i, column=j, padx=5, pady=5)

# Run the main loop
root.mainloop()

if __name__ == "__main__":
data = fetch_data()
display_data(data)