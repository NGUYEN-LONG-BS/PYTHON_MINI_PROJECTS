import pyodbc

def create_connection():
    
    server = '103.90.227.154'  # Replace with your server name
    database = 'BAN_KINH_DOANH'  # Replace with your database name
    username = 'sa'  # Replace with your SQL Server username
    password = 'Ta#9999'  # Replace with your password

    # SQL-Server connection string with Server Authentication
    conn = pyodbc.connect(
        f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};PORT=1433'
    )
    
    return conn