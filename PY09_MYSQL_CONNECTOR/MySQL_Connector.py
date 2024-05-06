# hai cú pháp cái đặt hiệu quả
# pip install mysql
# python -m pip install mysql-connector-python
# https://dev.mysql.com/downloads/installer/

import mysql.connector




db = mysql.connector.connect(user='root',password='Ta#9999',host='localhost')

#query
code='CREATE DATABASE `DB_USER_ID` ;' # 'CREATE SCHEMA `test` ;'

#RUN
mycursor=db.cursor()
mycursor.execute(code)