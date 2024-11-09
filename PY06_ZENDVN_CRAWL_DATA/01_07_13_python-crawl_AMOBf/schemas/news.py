def create_news_table(cursor, mydb):

    create_table_sql = """ CREATE TABLE IF NOT EXISTS news (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        link VARCHAR(255),
        image_link VARCHAR(255),
        description VARCHAR(255),
        content TEXT,
        time_crawl VARCHAR(255),
        special BOOLEAN DEFAULT FALSE,
        source_id INT
    ) """

    cursor.execute(create_table_sql)
    mydb.commit()
