import pyodbc

class Database:
    def __init__(self, server, database, username, password):
        self.connection = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
        )
        self.cursor = self.connection.cursor()

    def query(self, sql, params=()):
        self.cursor.execute(sql, params)
        self.connection.commit()
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
