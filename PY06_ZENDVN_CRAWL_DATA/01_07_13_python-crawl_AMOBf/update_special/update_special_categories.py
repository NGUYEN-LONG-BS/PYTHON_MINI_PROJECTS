import requests
from bs4 import BeautifulSoup

def update_special_in_db(cursor, mydb, category_name):
    sql = "UPDATE categories SET special = true WHERE name = %s"
    cursor.execute(sql, (category_name,))
    mydb.commit()

def update_special(cursor, mydb, link_main):
    response        = requests.get(link_main)
    soup            = BeautifulSoup(response.text, 'html.parser')

    category_li = soup.select("body > section:nth-child(8) > div > div > div > div > ul > li")

    for item in category_li:
        category_name = item.get_text().strip()

        update_special_in_db(cursor, mydb, category_name)

def main(cursor, mydb):
    link_main = 'http://demo-php-bookstore.zendvn.com'

    update_special(cursor, mydb, link_main)

    print("Update special categories: Finish!")