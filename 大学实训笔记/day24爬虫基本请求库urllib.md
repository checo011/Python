# 爬虫基本请求库 urllib

~~~markdown
Python有很多爬虫库：
HTTP请求库，解析库，异常库
~~~

* urllib

~~~markdown
1. 是内置的HTTP库
		urlib.request  : 请求库
		urllib.parse   ：解析库
		urllib.error   ：异常库
2. 目标：利用urllib库，完成爬虫任务
		爬虫学科，可以使用urllib 
~~~

### urllib库

~~~markdown
1. 三大模块：
		request：请求库
		error：异常库
		parse：解析库（url解析）
2. 基本使用：
		用于抓取网页
~~~

* 应用：

~~~markdown
1. urlopen(url)
		urllib.request.urlopen()
		通过url发送请求，获得一个response对象
		(如果要查看内容，需要调用response对象内部的方法和属性)
2. response对象（简称）
		全称：http.client.HTTPResponse
		1. read() : 读取响应中的响应内容，并打包成二进制字符串（bytes类型）返回
		2. encoding：  response.encoding='utf-8'   配置编码 在读之前调用
				和网页中的响应头： content type字段中的  charset 一致
		3. urlretrieve(url,filename)
				通过url得到的二进制数据，存储到filename指定的位置
				filename：全名：路径+名字+后缀
				          相对路径： 名字+后缀
		4. urlcleanup()
				释放网络资源  （最好在代码前后都添加，避免别的资源占用，避免占用别人的资源）
3. qute():
		urllib.parse.qute('汉字')
		将汉字转化为url可以识别的内容 
4. 官方提供的网络爬虫开发者测试网站： http://www.httpbin.org/ 
		可以测试请求类型，ip地址，cookies信息等等，根据官网的提示修改网址，即可测试
5. urlencode(数据字典):
		将数据字典，转化成url可识别的数据类型
~~~

~~~python
#########urlopen###########
import urllib.request as request

response=request.urlopen(url='http://www.baidu.com/')
# print(response)
response.encoding='utf-8'
html_bytes=response.read()
html_str=html_bytes.decode('utf-8') # 默认解码为utf-8
print(html_str)

# with open('hehe.html','w',encoding='utf-8') as f:
#     f.write(html_str)

#######二进制数据存储#################
import urllib.request as request

request.urlcleanup()  # 释放资源
url='https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1602553409&di=bcb1b5b06fa9b02719cab81bea3a1c9c&src=http://a3.att.hudong.com/14/75/01300000164186121366756803686.jpg'

request.urlretrieve(url=url,filename=r'G:\桌面所有文件\桌面\hehe.jpg')
request.urlcleanup()  # 释放资源


########发送get请求##################
import urllib.request as request
import urllib.parse as parse

# 发送get请求   # get请求的参数是通过url携带过去的  --明文请求
keyword=parse.quote('爬虫工程师')
# 1.发送请求
url=f'http://www.baidu.com/s?wd={keyword}'
response=request.urlopen(url=url)
# 2.获取响应
print(response.read().decode('utf-8'))

#########发送post请求################
import urllib.request as request
import urllib.parse as parse
# 1. 构建post数据
post_data={
    'name':'xiaobo',
    'pwd':'123'
}
# 2.将字典转换成url认识的类型 -- 尚未加密
post_data=parse.urlencode(post_data)
# 3. 加密 就是编码
post_data=post_data.encode('utf-8')

#4. 编辑url
url='http://www.httpbin.org/post'
# 5. 发送请求
response=request.urlopen(url=url,data=post_data)
print(response.read().decode('utf-8'))
~~~

* 小结

~~~markdown
1. 发送get请求流程：
		1. 导包
		2. 创建URL 对url整理： f'http://www.baidu.com/s?wd={参数内容}'
		3. res=urlopen(url=url)
		4. res.read().decode('utf-8')
2. 发送post请求流程：
		1. 导包
		2. 创建URL
		3. 准备数据字典
		4. parse.urlencode(数据字典)  # 将字典转化成url 识别的数据
		5. 加密： 编码 .encode()
		6. res=urlopen(url=url,data=加密数据)  # 将post数据传入请求中
		7. res.read().decode('utf-8')
~~~

---

### urllib库的高级用法

~~~markdown
1. 设置Headers
		1. 导包
		2. 配置url
		3. 创建headers数据字典
		4. 创建Request对象，把字典传入到Request参数中，url也一并传入
		5. res=urlopen(Request对象)
		6. res.read().decode('utf-8')
2. Proxy的设置   代理设置
		每一台计算机都有一个唯一的IP地址，反爬虫：封禁IP ，当前IP的计算机，无法访问指定网络
		1. 导包
		2. 配置url
		3. 创建代理数据字典
		4. 创建代理启动器
		5. 创建控制器并把代理启动器装载进去
		6. 装载控制器
		7. res=urlopen(Request对象)
		8. res.read().decode('utf-8')
3. cookies设置
		用于保持回话 
		cookies是服务端创建的，发送给客户端的数据
		在urllib中，默认没有可以接收cookie的容器
		使用http.cookiejar.CookieJar()对象给urllib构建一个容器，使得本应该接收的cookies信息可以得到接纳
		1. 导包
		2. 配置url
		3. 创建CookieJar对象
		4. 创建cookie处理器，传入CookieJar对象
		5. 创建代理启动器
		6. 装载启动器
		7. res=urlopen(Request对象)
		8. res.read().decode('utf-8')
~~~

~~~python
##########设置headers############
import urllib.request as request

url='http://www.httpbin.org/headers'
# 创建头信息字典
headers={
    'name':'xiaobo',
    'age':18,
    'gender':True
}
# 构建新的Request对象
r=request.Request(url=url,headers=headers)
# 把以前的url替换为新的Request对象 
response=request.urlopen(r)
#源码分析： urlopen--opener.open()
print(response.read().decode('utf-8'))

###########配置代理#############
'114.106.130.19	4237'

import urllib.request as request

request.urlcleanup()
# 设置代理数据字典
proxy={
    'http':'180.122.144.138:4253'
}
# 创建代理控制器
proxy_handler=request.ProxyHandler(proxy)
# 创建opener ,含有新的代理的启动器
opener=request.build_opener(proxy_handler)
# 将新opener 装载到启动器中
request.install_opener(opener)


url='http://www.httpbin.org/ip'
response=request.urlopen(url=url)  # opener.open()
print(response.read().decode('utf-8'))
request.urlcleanup()
"61.158.152.28"


########cookie设置#########
import urllib.request as request
import http.cookiejar as cookiejar

# 创建cookieJar对象
cj=cookiejar.CookieJar()
#Cookie处理器
cookis_processor=request.HTTPCookieProcessor(cj)
# 创建启动器
opener=request.build_opener(cookis_processor)
# 装载启动器
request.install_opener(opener)

url='http://www.httpbin.org/cookies/set?freeform=age%3A18'
response=request.urlopen(url=url)
print(response.read().decode('utf-8'))

~~~

---

