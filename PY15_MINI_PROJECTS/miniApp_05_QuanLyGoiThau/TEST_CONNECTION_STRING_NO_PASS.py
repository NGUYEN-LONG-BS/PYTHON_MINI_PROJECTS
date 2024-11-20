import pyodbc
conn = pyodbc.connect('Server=KSNB3\SQLEXPRESS;\
                      Database=DATABASE_USER_ID;\
                      Trusted_Connection=True;\
                      PORT=1433;\
                      DRIVER={SQL Server}')
cursor = conn.cursor()
cursor.execute('Select * from TB_DS_DATABASE')
rows = cursor.fetchall()
print(rows)
cursor.close()
conn.close()
# Test connect