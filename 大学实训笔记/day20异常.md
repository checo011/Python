# 异常

~~~markdown
容错性：允许犯错的性质
异常本质是Python中的类
异常一旦出现，则会终止程序运行（不论大小）
~~~

* 常见的异常类

~~~markdown
1. FileNotFoundError ：文件未找到异常
2. ValueError： 值异常
3. TypeError:类型错误
4. NameError： 名字异常
5. AttributeError：属性异常
6. AssertionError：断言异常
7. StopIteration：停止迭代异常
8. IndexError：索引异常
9. KeyError：键异常
10. SyntaxError：语法错误
11. RecursionError：递归错误
12. ZeroDivisionError： 0做分母（除数）异常
13. KeyboardInterrupt：键盘终止异常
~~~

* 异常之间的继承关系

~~~markdown
大多数异常：父类是Exception，
BaseException是所有异常类的父类
~~~

* 自定义异常

~~~markdown
1. 自己创建的异常类
2. 异常抛出：
		主动抛出异常：
		raise 异常的类名
3. 注意：
		1. 自定义异常，要定义一个类
		2. 该类必须直接或间接的继承于BaseException
		3. 尽量将错误信息封装到内部
		4. 使用raise 语句抛出异常
		5. 抛出异常：
				1. 抛出异常类
				2. 抛出异常对象
~~~

~~~python
class TicketSoldOutError(BaseException):
    def __init__(self):
        super().__init__(':票买完了！')
# raise ValueError

# class A:
#     pass

# print(A)
# print(__name__)

raise TicketSoldOutError()
~~~

* 异常的处理

~~~markdown
说明：
异常一旦出现，则会导致程序终止
异常处理可以保证，有异常的情况，可以继续运行，并可以合理处理异常信息

1. try-except结构 （基本）
		语法：
		try:
			可能出现异常的代码
		except 异常类名 as 变量:
			异常处理的代码
		
		变量： 变量是用于接收异常信息的变量
2. 特点：
		1. except后的异常名，必须是try中要抛出的异常
			如果异常名不包含实际抛出的异常，则正常报错
		2. 利用多态的思想except后的异常类，可以是该类或其子类
			捕获异常，可以捕获指定异常类或其子类异常的
		3. 注意：except后的类不要过大，因为会导致可读性差（不知道抛出的异常具体是什么类型）
		4. as 变量  可以省略的 
		5. except 后可以省略异常类名，表示默认捕获所有异常
3. try-except-except结构
		语法：
		try:
			可能出现异常的代码
		except 异常类名1 as 变量:
			异常处理的代码
        except 异常类名2 as 变量:
			异常处理的代码
4. 特点：
		1. 该结构中，try只能有一个，except可以有多个
		2. 大类型的except异常捕获应该尽量放到后面（否则导致后面的小类型异常无法捕获）
		3. 只要有一个except捕获到了异常，其他except则不再执行
5. try-finally
		语法：
		try:
			可能出现异常的代码
		finally:
			无论是否出现异常，都要执行的代码
6. try-except...-finally
		语法：
		try:
			可能出现异常的代码
		except 异常类名1 as 变量:
			异常处理的代码
        except 异常类名2 as 变量:
			异常处理的代码
		...
		finally:
			无论是否出现异常，都要执行的代码
7. try-except...-else-finally
		语法：
		try:
			可能出现异常的代码
		except 异常类名1 as 变量:
			异常处理的代码
        except 异常类名2 as 变量:
			异常处理的代码
		...
		else:
			如果没有报错，要执行的代码
		finally:
			无论是否出现异常，都要执行的代码
~~~

---



