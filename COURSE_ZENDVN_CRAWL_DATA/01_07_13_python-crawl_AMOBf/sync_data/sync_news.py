import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_all_news(cursor):
    cursor.execute("SELECT id, link, time_crawl FROM news")
    return cursor.fetchall()

def delete_news(cursor, mydb, news_id):
    sql = 'DELETE FROM news WHERE id = %s'
    cursor.execute(sql, (news_id,))
    mydb.commit()

def update_news(cursor, mydb, news_id, name, content, time_crawl):
    sql = "UPDATE news SET name = %s, content = %s, time_crawl = %s WHERE id = %s"
    cursor.execute(sql, (name, content, time_crawl, news_id))
    mydb.commit()

def update_or_delete_news(cursor, mydb, news_id, news_link, news_time_crawl, link_main):
    response             = requests.get(link_main + news_link)
    soup                 = BeautifulSoup(response.text, 'html.parser')
    error_element        = soup.select_one('body > section > div > div > div > div.error-section')
    time_crawl_current = soup.select_one('body > section > div > div > div.col-xl-9.col-lg-8.blog-detail > ul > li:nth-child(1)').text.strip()

    if error_element:
        delete_news(cursor, mydb, news_link)

    elif news_time_crawl != time_crawl_current:
        name                 = soup.select_one('body > section > div > div > div.col-xl-9.col-lg-8.blog-detail > h3').text.strip()
        content_element      = soup.select_one('body > section > div > div > div.col-xl-9.col-lg-8.blog-detail > div.ckeditor-content')
        list_content         = content_element.contents
        content              = ''.join(map(str, list_content))

        update_news(cursor, mydb, news_id, name, content, time_crawl_current)

def update_history(cursor, mydb, type):
    sql = """ UPDATE history SET time_sync = %s WHERE type = %s """

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(sql, (current_time, type))
    mydb.commit()

def main(cursor, mydb):
    link_main = 'http://demo-php-bookstore.zendvn.com'

    items_news = get_all_news(cursor)

    for news_id, news_link, news_time_crawl in items_news:
        update_or_delete_news(cursor, mydb, news_id, news_link, news_time_crawl, link_main)

    update_history(cursor, mydb, "news")
    print("Sync news: Finish!")

    