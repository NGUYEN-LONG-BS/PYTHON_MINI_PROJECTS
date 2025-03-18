def create_news_table(cursor, mydb):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS categories (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        link VARCHAR(255),
        special BOOLEAN DEFAULT FALSE,
        source_id INT
    ) """

    cursor.execute(create_table_sql)
    mydb.commit()