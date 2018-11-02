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

# c.execute('''CREATE TABLE BOOKS
# (ID INT PRIMARY KEY NOT NULL ,
# Name           TEXT NOT NULL ,
# Author         TEXT ,
# Country        TEXT ,
# Translator     TEXT ,
# Size           TEXT NOT NULL ,
# Time           TEXT NOT NULL ,
# MD5            TEXT NOT NULL ,
# SHA1           TEXT NOT NULL ,
# CRC32          TEXT NOT NULL
# );''')
#
# print("Table Create Success")

print("Opened database successfully")

c.execute("INSERT INTO BOOKS (ID, Name, Author, Country, Translator, Size, Time, MD5, SHA1, CRC32) VALUES (1,\
          'Python编程：从入门到实践-[美]埃里克·马瑟斯-[文字版].pdf', '', '', '', '20.9 MB (21,929,323 字节)', \
          '2018年11月1日 15:09:40', '6D2F56FEDDC4AA5EAD6366FA11AD2FC6', '0EA66E5432CB4EFF00B46BCD049E492EABF06462', \
          '2501DFAF')")


conn.commit()

print("Records created successfully")

conn.close()
