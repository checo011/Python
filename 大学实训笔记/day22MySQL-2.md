# MySQL2

* 基本数据操作SQL

~~~markdown
1. 增加
		insert into 表名（字段1，字段2.。。） values (值1，值2.。。)
2. 删除 
		delete from 表名 where 字段=值   
3. 修改
		update 表名 set 字段=值  where 字段=值
4. 查询
		select * from 表名     查询表中所有的字段和内容
		select 字段1，字段2, from 表名   查询表中指定的字段和内容
		select 字段1 as 别名，字段2 as 别名, from 表名    as可以省略
~~~

# MySQL 和 Python链接

1. 安装MySQL驱动

~~~markdown
1. mysql-connector-python 
		mysql 官方提供的驱动器 ，纯python构建的
2. PyMySQL
		纯python构建的
3. cymysql
		C构建的
4. mysqlclient:
		C构建的 
5. mysqldb：
		只能链接python2
~~~

* 驱动安装

~~~markdown
1. pip install mysqlclient  (推荐)
		无需手动下载安装包，无需点击安装过程，全部自动化，自动匹配版本号
		直接从网络安装
2. 设置版本号安装：
		pip install mysqlclient-1.3.12-cpt36-cp36m_amd64
		直接从网络下载安装
3. 以压缩包安装：
		pip install mysqlclient-1.3.12-cpt36-cp36m_amd64.whl
		本地安装
		
4. Pycharm安装
		file---settings---project interpreter---点击+号---搜索模块---选中模块---点击install Package  
		安装成功后，关闭即可（下方出现绿色提示）
		
pip 指令：
1. 下载并安装的指令：
		pip install 模块名  -i 'https://pypi.tuna.tsinghua.edu.cn/simple/'
2. 查看已经安装的所有模块(多有第三方模块)
		pip list      
3. 只下载，不安装
		pip download 模块名
4. 写在模块
		pip uninstall 模块名
~~~

---

2. 数据库操作API

~~~markdown
1. 获取连接
2. 获取游标对象
3. 准备SQL语句
4. 执行SQL语句
5. 事务提交
6. 关闭资源/释放资源

说明： 查询语句，需要通过cursor对象单独获取查到的数据
1. cursor.fetchone()
		返回一个数据，打包成元组
2. cursor.fetchall()
		返回所有数据，打包成二维元素
3. cursor.fetchmany(size)
		返回size个数据，打包成二维元素
		最少获取一条数据
4. cursor.execute(sql,[参数1，参数2])  
		可以避免SQL注入
~~~

~~~python
# 增删改查

import MySQLdb

# 1.连接数据库，获取conn
conn = MySQLdb.Connect(
    host='localhost',
    user='root',
    passwd='123',
    charset='utf8',
    port=3306,
    db='test'
)
# 2. 创建游标对象
cursor = conn.cursor()
# 3. 准备SQL
# sql='insert into user values ("admin","123")'
# sql='update user set pwd="456" where name="admin"'
# sql = 'delete from user where name="admin"'
name=input('账号：')
pwd=input('密码：')
sql='select name,pwd from user where name=%s or pwd=%s'
# 4. 执行SQL
result=cursor.execute(sql,[name,pwd])  # SQL语句受影响的行数
# 5. 事务提交
conn.commit()
# a=cursor.fetchone()  # 获取所有查询结果的第一条数据  打包成元组返回
# b=cursor.fetchall()   # 获取所有的查询结果，打包成二维元组返回
# print(a)
# print(b)
c=cursor.fetchmany(0)  # 获取所有查询结果，只返回指定的条数的数据内容 ，并打包成二维元组
print(c)
# 6. 关闭资源
cursor.close()
conn.close()
# print(result)
~~~

