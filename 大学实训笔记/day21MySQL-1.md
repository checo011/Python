# MySQL

### 简介

~~~markdown
数据库：存储数据
SQLServer  Oracle  Mysql 
RDB--关系型数据库   存储介质：硬盘  存储形式：文件形式
MySQL---Oracle   
MySQL：开元免费
Oracle：不开元，费用昂贵
MariaDB  DB2

NoSQL数据库：
非关系型数据库
Redis ：基于缓存，  MongoDB

MySQL：
结构：库  表  行  列   
MySQL中可以有多个数据库
每个库可以有多个表 
每个表： 多个列（字段）  多行数据
~~~

---

* 技术回顾

~~~markdown
1. 验证是否安装成功
		cmd--mysql -u root -p 回车 
		密码： 123456  000000  没有设置密码
		出现了Mysql版本号 成功
2. 设置初始密码：
		mysqladmin -u用户名 password "密码"
3. 修改密码：
		mysqladmin -u用户名 -p旧密码 password新密码
4. 忘记密码：
		1. 关闭正在运行的MySQL服务
		2. 打开cmd--跳转到mysql\bin
		3. 输入mysqld  --skip-grant-tables 回车
		4. 再开一个cmd窗口，输入mysql直接回车
		5. use mysql
		6. update user set password=passwrd("密码") where user="root"
		7. flush privileges
		8. quit;
		9. 重新登录即可
~~~

### 数据库管理

~~~markdown
1. 显示数据库所有的库
		show databases
2. 显示某一个小库中的所有表
		show tables
3. 创建数据库
		create database
4. 删除数据库
		drop database
~~~

### DDL操作

~~~markdown
DDL：Data Definition Language  ---建表语句
SQL：s: Structer Query Language
~~~

1. 创建表

~~~markdown
1. create table 表名（
	id int,
	name varchar(20),
）
~~~

2.  简单数据类型

~~~markdown
1. int/integer：整型
2. varchar（范围） ： 字符串
3. datetime ：时间格式
~~~

3. 简单约束

~~~markdown
1. auto_increment :自动增长
		MySQL会自动给新的数据编号
2. primary key :主键
		唯一标识数据库表中的每一条记录
		不重复且非空
3. not null : 非空
4. unique: 唯一
		可以是空值
~~~

4. 查看表结构

~~~markdown
desc 表名
~~~

5. 插入数据

~~~markdown
insert into 表名（字段名1，字段名2） values(值1，值2);
~~~

6. 查询语句

~~~markdown
select * from 表名;
~~~

---

