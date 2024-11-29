import pyodbc

def create_connection():
    # """Tạo kết nối đến SQL Server từ cấu hình"""
    # conn = pyodbc.connect(
    #     'DRIVER={ODBC Driver 17 for SQL Server};'
    #     'SERVER=103.90.227.154;'  # Thay bằng địa chỉ server của bạn
    #     'DATABASE=LA_2024;'  # Thay bằng tên database của bạn
    #     'UID=sa;'  # Thay bằng username của bạn
    #     'PWD=Ta@9999;'  # Thay bằng password của bạn
    # )
    
    
    # # Connection details
    # server = 'KSNB3\\SQLEXPRESS'  # Replace with your server name
    # database = 'DATABASE_USER_ID'  # Replace with your database name
    # username = 'sa'  # Replace with your SQL Server username
    # password = 'Ta#9999'  # Replace with your password
    
    server = '103.90.227.154'  # Replace with your server name
    database = 'LA_2024'  # Replace with your database name
    username = 'sa'  # Replace with your SQL Server username
    password = 'Ta#9999'  # Replace with your password

    # SQL Server Authentication
    conn = pyodbc.connect(
        f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};PORT=1433'
    )

    # # Uncomment this if you want to use Windows Authentication instead:
    # conn = pyodbc.connect(
    #     f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;PORT=1433'
    # )
    
    return conn