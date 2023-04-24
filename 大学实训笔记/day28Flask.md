# Flask

* 简介

~~~markdown
Flask是一个Python语言编写的Web微框架
常用的开发模式： MVC 
		M:module 模板
        V:view   视图
        C:controler 控制器（核心主控程序）
		重量级：组件多，代码量（大），消耗的的资源多
		轻量级：组件少
~~~

* 安装

~~~markdown
1. 第三方框架：
		pip install flask
2. 需要其他依赖：
		werkzeug ： pip install werkzeug
		是一个WSGI（在Web应用和多种服务器之间的一种标准Python接口）
		jinja2:     pip install jinja2
		jinja负责模板渲染
~~~

* hello world

~~~Python
from flask import Flask

# 初始化app
app = Flask(__name__)

# 配置路由
@app.route('/')    # 必须配置
def index():  # 配置函数 ，名字随意
    return 'hello world'


# 配置路由
@app.route('/hehe')    # 必须配置
def hehe():  # 配置函数 ，名字随意
    return 'HEHEHE'

#
if __name__ == '__main__':
    app.run()
~~~

* 路由配置

~~~python
作用：使用app.route()装饰器，把一个函数绑定到对应URL上

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index1():
    return 'hello world'

@app.route('/hello/hehe/')
def index2():
    return 'Hello Python'

@app.route('/hello/hehe2')
def index3():
    print()
    return 'hehe2'

if __name__ == '__main__':
    app.run(debug=True)
~~~

* 配置Templates

~~~python
Templates是一个文件夹，里面存放所有要展示的页面或数据


from flask import Flask
from flask import render_template   # 模板渲染

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/echarts/')
def get_bar():
    return render_template('bar_base.html')


if __name__ == '__main__':
    app.run(debug=True)
~~~

* 参数传递

~~~python
# 前端向服务端传递数据

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods=['GET'])
def login():
    # 获取get请求中的参数
    name = request.args.get('name')
    pwd = request.args.get('pwd')

    if name=='admin' and pwd=='123':
            return '登录成功'
    else:
        return '登录失败'

@app.route('/login_post/',methods=['POST'])
def login_post():
    # 获取get请求中的参数
    name = request.form.get('name')
    pwd = request.form.get('pwd')

    if name=='admin' and pwd=='123':
            return '登录成功'
    else:
        return '登录失败'

if __name__ == '__main__':
    app.run()
    
    
    
    
    
## 后端服务器向前端传递数据
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_post/',methods=['POST'])
def login_post():
    # 获取get请求中的参数
    name = request.form.get('name')
    pwd = request.form.get('pwd')

    if name=='admin' and pwd=='123':
            return render_template('login_success.html',welcome_name=name)
    else:
        return '登录失败'

if __name__ == '__main__':
    app.run()
~~~

