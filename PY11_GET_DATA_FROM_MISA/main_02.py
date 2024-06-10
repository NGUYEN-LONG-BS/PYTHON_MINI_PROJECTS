import pyodbc


VAR_SQL_DRIVER = "{SQL Server Native Client 11.0}"
VAR_SERVER_NAME = "KSNB3\SQLEXPRESS"
VAR_DATABASE_NAME = "DATABASE_USER_ID"
VAR_SQL_QUERY = "select * from TB_DS_DATABASE"

#Define Connection String'
sqlDbConn = pyodbc.connect(
    "Driver= {SQL Server Native Client 11.0};"      # SQL Server version 2012-2014
    "Server="& VAR_SERVER_NAME &";"
    "Database="& VAR_DATABASE_NAME &";"
    "Trusted_Connection=yes; ")

def getData(sqlDbConn):
    print("Read")
    cursor = sqlDbConn.cursor(); 
    cursor.execute(VAR_SQL_QUERY)
    for row in cursor:
        print(f'{row}')

getData(sqlDbConn);                 # Bước 1: Read: kết nối đến SQL Server và lấy dữ liệu về

