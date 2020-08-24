# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description:
import pymysql
from pymysql.cursors import DictCursor

# 连接数据库
conn = pymysql.connect(host='192.168.75.3', port=3306, user='root', passwd='123456', db='test', charset='utf8')
# 建立游标，返回字典
cur = conn.cursor(DictCursor)
# sql操作
sql = "select * from user"
# 执行sql
cur.execute(sql)
# 获取执行结果
res = cur.fetchall()
# 打印结果
print(res)
# 关闭游标
cur.close()
# 关闭数据库连接
conn.close()
