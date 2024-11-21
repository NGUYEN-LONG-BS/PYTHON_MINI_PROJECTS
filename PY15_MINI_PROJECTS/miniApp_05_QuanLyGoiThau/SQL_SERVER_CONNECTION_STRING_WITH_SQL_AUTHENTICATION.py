import pyodbc

# Connection details
server = '103.90.227.154'
database = 'LA_2024'
username = 'sa'
password = 'Ta#9999'  # Replace with your actual password

# Connection string with SQL authentication
conn = pyodbc.connect(
f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};PORT=1433'
)

# Create a cursor and execute a query
cursor = conn.cursor()
cursor.execute('SELECT * FROM [LA_2024].[dbo].[TB_COMPONENT_CATEGORIES]')
rows = cursor.fetchall()

# Print the results
print(rows)

# Close the cursor and connection
cursor.close()
conn.close()