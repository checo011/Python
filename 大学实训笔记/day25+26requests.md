# requests  模块 高级请求库

~~~markdown
1. 基于urllib编写的HTTP请求库
		requests底层封装了urllib
2. 更加具有Python的风格，更加人性化，简单易用
3. 爬虫业务中最常用的库
4. 是第三方的库
		pip install requests
~~~

* requests模块的属性

~~~markdown
1. get(url,params=None,**kwargs):
		发送get请求
		url: 访问的路径
		params：给请求传递的参数  可以是字典或二进制数据
		**kwargs：本质是给request()传递的参数
2. post(url, data=None, json=None, **kwargs)
		发送post请求
		url：访问路径
		data: 请求参数 
		json： json数据
		**kwargs：本质是给request()传递的参数
3. request(method, url, **kwargs)
		method:字符串，说明发送的请求模式
		url: 请求路径
		
4. put()
5. delete()
~~~

* response对象

~~~markdown
1. reqeusts模块发送请求会获得响应对象-response对象
2. response的常用属性
		1. text  返回响应的文本数据（str）
		2. content 返回响应的二进制数据（bytes）
		3. encoding  设置编码
		4. status_code  返回状态码
		5. apparent_encoding 分析响应编码
		6. headers  获取响应头信息
		7. cookies  获取响应的cookie信息
		8. elapsed  耗时
		9. history	返回调整历史
		10. url     返回当前请求地址
		11. json    采用json的格式输出响应内容
~~~

* 设置headers

* 设置proxy

~~~python
import requests

url='http://www.httpbin.org/ip'
# 设置代理字典：
proxies={
    'http':'115.209.195.139:4285'
}
response=requests.get(url=url,proxies=proxies)
print(response.text)

~~~

* session发送请求

~~~python
import requests

# get   post  reqeuest  session
url='http://www.baidu.com/'
s=requests.Session()
response=s.get(url=url)
response.encoding=response.apparent_encoding
print(response.text)
~~~

* with-session格式

~~~python
import requests

url='http://www.baidu.com'
with requests.Session() as session:
    response=session.get(url=url)
    response.encoding=response.apparent_encoding
    print(response.text)
~~~

* session配置headers

~~~python
import requests

url='http://www.httpbin.org/headers'
headers={
    'name':'xiaobo'
}
with requests.Session() as session:
    # 将 headers信息，永久配置到session,只要发送请求，会自动携带数据
    session.headers=headers
    # 第一次请求
    print(session.get(url=url,headers={'name':'18'}).text)
    # 第二次请求
    print(session.get(url=url).text)

# print(requests.get(url=url, headers=headers).text)

# 如果临时数据和全局数据同名，临时的覆盖全局的数据
~~~

* session设置cookie

~~~python
import requests

url='http://www.httpbin.org/cookies'
with requests.Session() as session:
    session.cookies.update({'name':'xiaobo'})
    print(session.get(url=url).text)
~~~

---

