# 正则表达式

~~~markdown
1. 运行在语言环境中
2. 解析字符串，效率很高
~~~

* 正则表达式的概念

~~~markdown
正则表达式是一种小型的，高度专业化的编程语言，内嵌在Python中，通过re模块来实现
1. 可以为想要匹配的字符串指定查找规则
2. 可以利用RE模块用多种方式修改或查找字符串
运行原理：
1. 被编译成一系列的字节码，由C语言编写的匹配引擎进行执行
2. 正则表达式不能匹配一切字符(不是任何时候都可以用正则)
~~~

* re模块

~~~markdown
findall(正则表达式,目标字符串) --》 返回匹配到的字符串列表
1. 普通字符串：
		大多数字母和字符都可以匹配自身
元字符串：
2. [ ] :
		1. 用来指定一个字符集
				[abcde]  [a-z]
		2. 表示一个值范围 
				[0-9]
		3. 补集：
				[^ab] #除了ab的都可以
		4. 在字符集中其他元字符只体现字符串本身的作用
3. ^ 
		匹配行首
				^ab
4. $   
		匹配行尾
				ab$
5. + 
		匹配一个或多个字符
				c+   匹配一个或多个c的形式
6. *    
		匹配0个或多个字符
				c*  匹配0个或多个C   能多取就多取 ---贪婪模式
7. ？  
		匹配0个或1个
				单独使用：
				c?  匹配0个或1个C  默认---贪婪模式
				配合重复元字符使用：开启指定元字符的非贪婪模式
				？？  +？  *？ 
8. .   
		匹配除了换行符以外的任意字符
9. ( )  
		分组
		优先返回圆括号内的数据
10. \    反斜杠
 		1. \字母 特殊含义
 			\d 匹配十进制数
 			\D 匹配非十进制数
 			\s 匹配任何空白字符串 ：\r \n \t \f 
 			\S 同上取反
 			\w 匹配任何字母和字符   （最常用）
 			\W 同上取反
 		2. 取消转义
 			
11. {n} 
		指定重复数量
			\d{4}
~~~

---

* 爬取百度图片

~~~python
import re
import urllib.request as u # 请求库

# 找到图片网页的地址
url='https://image.baidu.com/search/index?ct=201326592&z=3&tn=baiduimage&ipn=r&word=%E7%8C%AB%E5%92%AA&p=60'
# url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1602146458615_R&pv=&ic=&nc=1&z=3&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=0&height=0&face=0&istype=2&ie=utf-8&sid=&word=%E7%8C%AB%E5%92%AA'
# 传入一个url，向该路径发起请求，返回服务端传过来的 响应对象
response = u.urlopen(url=url)
response.encoding='utf-8'
# 直接获取的网页数据本质都是二进制字符串
# 将二进制的网页源码，转换成Python可以操作的普通字符串
html=response.read().decode()
# print(html)

url_list=re.findall('thumbURL":"(http.*?\.jpg)',html)
print(url_list)
n=0
for img_url in url_list:
    n+=1
    u.urlretrieve(img_url,'%s.jpg'%n)

~~~

