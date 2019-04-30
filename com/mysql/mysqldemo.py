#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

db = pymysql.connect('localhost','root','xhua')
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchall()
print data
db.close()