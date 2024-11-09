def create_products_table(cursor, mydb):    

    create_table_sql = """ CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        link VARCHAR(255),
        image_link VARCHAR(255),
        image_name VARCHAR(255),
        price_current INT,
        price_old INT,
        category_id INT,
        content TEXT,
        special BOOLEAN DEFAULT FALSE,
        source_id INT,
        FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
    ) """

    cursor.execute(create_table_sql)
    mydb.commit()