def create_history_table(cursor, mydb):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS history (
        id INT AUTO_INCREMENT PRIMARY KEY,
        type VARCHAR(255),
        time_get DATETIME,
        time_sync DATETIME
    ) """

    cursor.execute(create_table_sql)
    mydb.commit()