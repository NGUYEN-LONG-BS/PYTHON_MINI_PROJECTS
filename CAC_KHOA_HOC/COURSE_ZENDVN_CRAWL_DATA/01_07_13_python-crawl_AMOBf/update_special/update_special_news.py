import requests
from bs4 import BeautifulSoup
from helpers import get_id

def update_special_in_db(cursor, mydb, source_id):
    sql = "UPDATE news SET special = true WHERE source_id = %s"
    cursor.execute(sql, (source_id,))
    mydb.commit()

def update_special(cursor, mydb, link_main):
    response        = requests.get(link_main)
    soup            = BeautifulSoup(response.text, 'html.parser')

    items_news = soup.select(".slide-3 > div")

    for item in items_news:
        link = item.find('a')['href']
        source_id = get_id(link)
        update_special_in_db(cursor, mydb, source_id)

def main(cursor, mydb):
    link_main = 'http://demo-php-bookstore.zendvn.com'

    update_special(cursor, mydb, link_main)

    print("Update special news: Finish!")