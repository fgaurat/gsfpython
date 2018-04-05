# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'admin',
    'password': 'mypass',
    'host': 'ns349423.ip-94-23-40.eu',
    'database': ''
}

cnx = cur = None
try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cur = cnx.cursor()
    cur.execute('show databases;')
    for row in cur.fetchall():
        print(row)
finally:
    if cur:
        cur.close()
    if cnx:
        cnx.close()