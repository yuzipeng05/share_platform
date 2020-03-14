# coding=utf-8
# @公众号 : "鹏哥贼优秀"
# @Date : 2020/3/14
# @Software : PyCharm 
# @Python version: Python 3.7.2


import sqlite3

tablename = "share_status"
con = sqlite3.connect('share_status.db', check_same_thread=False)
cur = con.cursor()

def create():
    sql = 'create table {0} (status)'.format(tablename)
    result = cur.execute(sql)
    con.commit()
    return True if result else False

def insert():
    sql = 'insert into {0} (status) values (0)'.format(tablename)
    result = cur.execute(sql)
    con.commit()
    return  True if result else False

def query():
    sql = 'select * from {0}'.format(tablename)
    result = cur.execute(sql)
    return str(list(result)[0][0])

def update(new_status):
    sql = 'update {0} set status={1}'.format(tablename,new_status)
    result = cur.execute(sql)
    con.commit()
    return True if result else False

if __name__ == "__main__":
    # create()
    # insert()
    update('0')
    print(query())