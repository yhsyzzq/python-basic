import pymysql, pprint

# 连接mysql数据库

# 创建连接，指定数据库的ip地址，账号、密码、端口号、要操作的数据库、字符集
conn = pymysql.connect(host='10.230.28.222', port=3306, user='root', passwd='111111', db='galaxy_new', charset='utf8')
# 创建游标
cursor = conn.cursor()
# 执行sql，并返回影响行数
selectSql = 'select * from galaxy_menu order by function_code'
cursor.execute(selectSql)
# 获取查询结果的第一行数据
firstRow = cursor.fetchone()
print(firstRow)

# 获取多行结果
firstThreeRow = cursor.fetchmany(3)
pprint.pprint(firstThreeRow)

# 获取所有结果
allRow = cursor.fetchall()
for row in allRow:
    print(('菜单名称：' + row[3]).ljust(20))
print('第一次查询结束')

countSql = 'select count(1) from galaxy_menu'
cursor.execute(countSql)
resultRow = cursor.fetchone()
print("查询记录数：%d" % resultRow[0])
# 关闭游标
cursor.close()

# 关闭连接
conn.close()
