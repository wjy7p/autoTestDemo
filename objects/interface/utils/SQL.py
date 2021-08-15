import pymysql


def search(sql):
    db = pymysql.connect(host="10.10.15.168", user="wpg", password="Wpg@_@MySQL2oIg", db="waterdb_ys")
    #使 用cursor c()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
    res = cursor.fetchall()
    db.close()
    return res

def search_171(sql):
    db = pymysql.connect(host="10.10.15.171", user="root", password="root", db="waterdb_ys")
    #使 用cursor c()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
    res = cursor.fetchall()
    db.close()
    return res


