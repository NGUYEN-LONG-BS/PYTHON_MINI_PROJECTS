import pyodbc
from define import *

#Define Connection String'
sqlDbConn = pyodbc.connect(
    "Driver= {SQL Server Native Client 11.0};"      # SQL Server version 2012-2014
    "Server=KSNB3\SQLEXPRESS;"
    "Database=" & VAR_DATABASE_NAME & ";"
    "Trusted_Connection=yes; ")

def getData(sqlDbConn):
    print("Read")
    cursor = sqlDbConn.cursor(); 
    cursor.execute(VAR_SQL_QUERY)
    for row in cursor:
        print(f'{row}')

getData(sqlDbConn);                