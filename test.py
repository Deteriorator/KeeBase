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

# c.execute("INSERT INTO BOOKS (ID, Name, Author, Country, Translator, Size, Time, MD5, SHA1, CRC32) VALUES (1,\
#           'Python编程：从入门到实践-[美]埃里克·马瑟斯-[文字版].pdf', '', '', '', '20.9 MB (21,929,323 字节)', \
#           '2018年11月1日 15:09:40', '6D2F56FEDDC4AA5EAD6366FA11AD2FC6', '0EA66E5432CB4EFF00B46BCD049E492EABF06462', \
#           '2501DFAF')")


# conn.commit()

# print("Records created successfully")

c.execute("UPDATE BOOKS SET Country = '美' WHERE ID=1;")

conn.commit()

print("Total number of rows updated:", conn.total_changes)

cursor = c.execute("SELECT ID, Name, Author, Country, Translator, Size, Time, MD5, SHA1, CRC32 FROM BOOKS;")
for row in cursor:
    print("ID = ", row[0])
    print("Name = ", row[1])
    print("Author = ", row[2])
    print("Country = ", row[3])
    print("Translator = ", row[4])
    print("Size = ", row[5])
    print("Time = ", row[6])
    print("MD5 = ", row[7])
    print("SHA1 = ", row[8])
    print("CRC32 = ", row[9])
print("Operation done succeddfully")
conn.close()
