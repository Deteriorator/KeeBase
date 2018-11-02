# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :        Liangz
   Date：          2018/11/2
-------------------------------------------------
   Change Activity:
                   2018/11/2:
-------------------------------------------------
"""
__author__ = 'Liangz'


import sqlite3


conn = sqlite3.connect('KeeBase.db')

print("打开数据库")

c = conn.cursor()

c.execute('''CREATE TABLE BOOKS
(ID INT PRIMARY KEY NOT NULL ,
Name           TEXT NOT NULL ,
Author         TEXT ,
Country        TEXT ,
Translator     TEXT ,
Size           TEXT NOT NULL ,
Time           TEXT NOT NULL ,
MD5            TEXT NOT NULL ,
SHA1           TEXT NOT NULL ,
CRC32          TEXT NOT NULL
);''')

print("Table Create Success")

conn.commit()
conn.close()
