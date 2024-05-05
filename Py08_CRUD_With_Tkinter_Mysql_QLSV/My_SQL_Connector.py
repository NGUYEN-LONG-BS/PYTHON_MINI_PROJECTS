# pip install mysql
# pip install mysql-connector-python
# python -m pip install mysql-connector-python
# py -3.12 -m pip install mysql-connector-python
# pip3 install mysql-connector-python-rf
# https://dev.mysql.com/downloads/installer/


import mysql.connector

print('hehehehehehehhehehehehe')

user_name_my_sql = 'root'
pass_my_sql = 'Ta#9999'
host_my_sql = 'localhost'   # 3306

db = mysql.connector.connect(user='root',password='Ta#9999',host='localhost')

#query
code='CREATE DATABASE `test` ;' # 'CREATE SCHEMA `test` ;'

#RUN
mycursor=db.cursor()
mycursor.execute(code)
