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
		url: 访问的路径
		params：给请求传递的参数  可以是字典或二进制数据
		**kwargs：本质是给request()传递的参数
2. post(url, data=None, json=None, **kwargs)
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

~~~

