#!/usr/bin/python35
# -*- coding: utf-8 -*-
# author: WangDaWei

import pymysql

conn = pymysql.connect(host='118.190.209.102', port=5700, user='root', passwd='123456', charset='utf8')

cursor = conn.cursor()
sql = "show databases"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
