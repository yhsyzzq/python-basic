import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
import cx_Oracle

# oracle数据库操作
print("cx_Oracle.version:", cx_Oracle.version)
# dsn = cx_Oracle.makedsn("192.168.218.56", 1521, "etldemo")
# conn = cx_Oracle.connect("search56", "search56", dsn)
#
# cursor = conn.cursor()  # 返回连接的游标对象
# # 执行查询
# selectSql = "select * from bi_web.t_auth_function order by bi_web.function_code"
# cursor.execute(selectSql)
# # 获取结果
# resultRow = cursor.fetchone()
# print(resultRow)
# cursor.close()
# conn.close()

# 获取oracle数据库连接


# 获取oracle数据库连接
conn = cx_Oracle.connect('search56/search56@192.168.218.56/etldemo')
# 获取游标
cursor = conn.cursor();
# 执行查询
selectSql = "select * from bi_web.t_auth_function order by function_code"
cursor.execute(selectSql)
# 获取结果
resultRow = cursor.fetchone()
print(resultRow)
cursor.close()
conn.close()
#
#
# print("cx_Oracle.version:", cx_Oracle.version)
# host = "127.0.0.1"
# port = "1521"
# sid = "databasetopaz"
# dsn = cx_Oracle.makedsn(host, port, sid)
# connection = cx_Oracle.connect("scott", "tiger", dsn)
# cursor = cx_Oracle.Cursor(connection)  # 返回连接的游标对象
# print("======")
