#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


def openDatabase(dbsrc):
    # 打开一个数据库，如果没有则会自动创建一个，
    # conn = sqlite3.connect(dbsrc)  # 在当前位置，创建（硬盘上）
    # conn = sqlite3.connect('memory')#在内存中创建（RAM）
    print("Opened database successfully")
    

def createTable(dbsrc):
    conn = sqlite3.connect(dbsrc)
    print("Opened database successfully")

    conn.execute('''CREATE TABLE COMPANY
       (ID  integer PRIMARY KEY autoincrement,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
    print("Table created successfully")

    conn.close()


def dropTable(dbsrc):
    conn = sqlite3.connect(dbsrc)
    print("Drop database successfully")

    conn.execute("drop table user")
    conn.commit()
    print("Table droped successfully")

    conn.close()


def insertRow(dbsrc):
    conn = sqlite3.connect(dbsrc)
    print("Opened database successfully")

    conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
        VALUES ('Paul', 32, 'California', 20000.00 )")

    conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
        VALUES ('Allen', 25, 'Texas', 15000.00 )")

    conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
        VALUES ('Teddy', 23, 'Norway', 20000.00 )")

    conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
        VALUES ('Mark', 25, 'Rich-Mond ', 65000.00 )")

    conn.commit()
    print("Records created successfully")
    conn.close()


def selectRow(dbsrc):
    conn = sqlite3.connect(dbsrc)
    print("Opened database successfully")

    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()


def updateRow(dbsrc):
    conn = sqlite3.connect(dbsrc)
    print("Opened database successfully")
    cursor = conn.cursor()
    #conn.execute("UPDATE COMPANY set SALARY = 250.00 where ID=1")
    cursor.execute("UPDATE COMPANY set SALARY = '2501.00' where ID=1")
    cursor.close()

    conn.commit

    print("Total number of rows updated :", conn.total_changes)

    conn.close()


def deleteRow(dbsrc):
    conn = sqlite3.connect(dbsrc)
    print("Opened database successfully")

    conn.execute("DELETE from COMPANY where ID=8;")
    conn.commit
    print("Total number of rows deleted :", conn.total_changes)

    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()


# 主函数
if __name__ == '__main__':
    src = "D:\\workspace\\PythonTester\\resources\\dbtester.db"
    #createTable(src)
    #insertRow(src)

    # updateRow(src)
    selectRow(src)
    # deleteRow(src)
    # dropTable(src)
