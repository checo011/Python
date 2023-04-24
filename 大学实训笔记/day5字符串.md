# 字符串（str）

* 特点

~~~markdown
1. 字符串天生具有跨平台特性
2. 字符串是不可变类型
~~~

* 创建

~~~markdown
1. 手工创建
		s='abc'
		''  :空字符串  简称：空串 
2. 构造方法
		1. str() :创建一个新的空字符串
		2. str(obj) :
				将任何对象转化成字符串
~~~

* 字符串的分类

~~~markdown
1. 单引号字符串  str
2. 双引号字符串  str
		双引号字符串，最终会被解析为单引号字符串
3. 三引号字符串  str
		多行字符串
		常常用于文档注释
4. 转义字符串：  str
		'\\'  \
		'\n'  换行
		'\t'  横向制表符 tab
		'\b'  退格符
		'\a'  启动蜂鸣器
		'\r'  换行符：windows特有
		'\v'  纵向制表符
		'\f'  换页符
5. 原始字符串： str
		r'abc'
		让所有的转义字符失效，体现字符串本来的功能
		原始字符串的最后不能写斜杠
6. unicode字符串 str
		u'abc' 
		该字符串使用unicode编码
7. 格式化字符串： str  format字符串
		f'abc'
		a=100
		s = f'I can eat {a} bread'
8. 二进制字符串 bytes
		b'abc'
		bytes-str: bytes.decode() 解码
		str-bytes: str.encode() 编码
~~~

* 访问

~~~markdown
1. 访问一个
		下标操作：
		s='abc'
		s[0] # 'a'
2. 访问多个
		切片操作
3. 访问所有
		遍历
~~~

* 其他方法

~~~markdown
1. upper():
		将字符串大写
2. lower():
		将字符串小写
3. strip(s):
		从字符串的两端去除s字符串
4. split(s):
		将字符串以s进行分割，并将分割号的数据打包成列表进行返回
5. join(iterable):
		s='*'
        print(s.join('abc'))
        print(s.join(['a','b','c']))
        # a*b*c
        将s作为插入元素，插入到可迭代对象的每一个元素之间，并打包成字符串返回
~~~

* 格式化字符串

~~~markdown
%s
1. 'I Love %s Forever'%Python
		I Love Python Forever
2. print(' %s and %s are friends'%('飞哥','小波'))
		多个参数要用逗号隔开
~~~

---

