# BeautifulSoup

~~~markdown
1. BeautifulSoup是一个可以从HTML或XML中提取数据的Python
		HTML，XML
2. 将HTML中的标签，看做是对象的形式，解析
3. 简称BS
4. 安装：
		pip install bs4
		pip install lxml
~~~

* BS的四种解析器

~~~markdown
1. Python标准库 
		解析速度适中，容错能力强
2. lxml-HTML 
		解析速度快，需要C语言环境
3. lxml-XML
		解析速度快，需要C语言环境，唯一一个可以解析XML
4. html5lib
		最好的容错性，慢
~~~

* 应用

~~~markdown
1. 对象：
		1. Tag ：标签
		2. NavigableSting  内容对象
		3. BeautifulSoup对象  文档对象  html
		4. Comment 注释对象
2. 基本使用
		1.标签操作
        	soup.标签名
			如果有多个同名标签，只会返回第一个
		2. 属性操作：
			soup.标签名[属性名]
		3. 内容操作
			soup.标签名.string
3. 常用操作：
		1. soup.findall(name=None，attrs={})
				name:标签名
				attrs:查找的属性参数  字典
				
~~~

