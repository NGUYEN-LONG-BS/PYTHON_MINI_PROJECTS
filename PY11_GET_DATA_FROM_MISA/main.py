import pyodbc
from define import *

#Define Connection String'
# sqlDbConn = pyodbc.connect(VAR_CONNECTION_STRING_TO_SQL_SERVER_WITH_WINDOWS_AUTHENTICATION)
sqlDbConn = pyodbc.connect(VAR_CONNECTION_STRING_TO_SQL_SERVER_WITH_SQL_SERVER_AUTHENTICATION)


def getData(sqlDbConn):
    cursor = sqlDbConn.cursor(); 
    cursor.execute(VAR_SQL_QUERY_02)
    for row in cursor:
        print(f'{row}')

getData(sqlDbConn);