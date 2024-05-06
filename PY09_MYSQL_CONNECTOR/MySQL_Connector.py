# hai cú pháp cái đặt hiệu quả
# pip install mysql
# python -m pip install mysql-connector-python
# https://dev.mysql.com/downloads/installer/

import mysql.connector
from Define_MySQL import * 



db = mysql.connector.connect(user='root',password='Ta#9999',host='localhost')


print('====================================================================hehehe===========')
#RUN
# mycursor=db.cursor()
# mycursor.execute(code)