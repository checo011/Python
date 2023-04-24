# 流程控制

### 条件分支流程

* if - else结构

~~~markdown
1. if 
		if 布尔表达式:
			代码
		含义：如果布尔表达式为真则执行代码，否则不执行
2. if - else
		if 布尔表达式:
			代码
		else :
			代码
		含义：如果布尔表达式为真则执行代码，否则执行else中的代码
3. if - elif - else
		if 布尔表达式:
			代码1
		elif 布尔表达式：
			代码2
		。。。			
		else :（根据情况可以省略）
			代码
		含义：如果布尔表达式为真则执行代码，否则在后续的elif中继续判断，当条件为真的elif满足时，则执行对应的代码

代码块：
Python支持分号和花括号的使用
{}：代码块---逻辑代码要写在代码块中
Python: 可以省略{}，用缩进的形式表示代码块（严格）

注意：
1. 每一套if-else  中 有且只有一个if语句
2. 每套if-else 中可以有else，但是最多只能有一个
3. 每套if-else 中可以有多个elif

嵌套结构
if-else结构中可以任意嵌套任意层if-else结构
~~~

* 断言assert

~~~markdown
用于系统流程控制
1. assert 布尔表达式
		含义：如果布尔表达式为真： 什么都不发生
			 如果布尔表达式为假：直接抛出异常： AssertionError
~~~

### 循环流程

* while循环

~~~markdown
重复操作
1. 语法:
		while 布尔表达式:
			代码（循环体）
		含义：while 先判断布尔表达式，如果为真，则执行循环，本次循环结束后，继续对布尔表达式进行判断，直到布尔表达式为假，循环停止
2. 死循环
		循环代码无限的执行
		何时会用到死循环：服务器，硬件的执行，操作系统
3. 控制循环的停止： 
		控制好循环停止的条件
4. while 常常用于不计数循环（不知道循环次数）
~~~

* for循环

~~~markdown
1. 定义： 
		计数循环
		常常用于已知循环次数的情况
2. 语法：
		for 变量 in 可迭代对象：
			循环体
		
		可迭代对象：有自己的元素,并且元素可以被访问，是一个容器	
		含义：每一次循环，将可迭代对象的每一个元素给变量赋值，并执行一次循环体，一次循环执行完毕后，for循环会向可迭代对象的下一个元素发起访问，如果元素存在则继续执行循环，如果元素不存在则结束循环
		
3. for循环的循环次数，和可迭代对象的元素的个数有关
		1. 循环的循环次数是元素个数+1次
		2. 循环体执行了元素个数次
4. 变量本质上只被创建了一次
5. for循环可以提供：
		1. 循环次数 （一定关注）
		2. 循环提供的数据 （可选关注）
~~~

* range对象

~~~markdown
1. range(stop)
		返回一个range类型的对象,
		range对象是一个可迭代对象
		其中start默认为0  
		取值范围：
		[0，stop)
2. range(start,stop,[step])
		返回一个range类型的对象
		step：默认是1,step是可选的
		取值范围：
		[start，stop)
		
3. range常常和for循环一起使用
~~~

* break

~~~markdown
跳出本层循环，其他循环本层不再执行
~~~

* continue

~~~markdown
跳过本次循环，其他本层循环继续执行
~~~

~~~python
# for i in range(5):
#     if i==2:
#         break
#     else:
#         print(i)


for i in range(5):
    if i==2:
        continue
    else:
        print(i)
~~~

* 循环嵌套

~~~markdown
循环里面可以嵌套循环
~~~

~~~python
# print('*',end='')
# print('*',end='')
# print('*',end='')
# print('*',end='')
# print('*',end='')
#
# for i in range(5):
#     print('*', end=' ')
# print()
#
# for i in range(5):
#     print('*', end=' ')
# print()
#
# for i in range(5):
#     print('*', end=' ')
# print()
#
# for i in range(5):
#     print('*', end=' ')
# print()
#
# for i in range(5):
#     print('*', end=' ')
# print()

# for i in range(5):  # 行  #
# #     for j in range(5):  # 每一行 有几列  列
# #         print('*', end=' ')
# #     print()

# 三角形：  推论：第n行 就有n个星号   行从1开始的

for i in range(1,6):  # 行  # 1-5  行号： 从1开始
    for j in range(i):  # 每一行 有几列  列  # 每一行 星号的数量和行号一样
        print('1*1=1', end=' ')
    print()

# 九九乘法表

for i in range(1,10):  # 行  # 1-5  行号： 从1开始
    for j in range(1,i+1):  # 每一行 有几列  列  # 每一行 星号的数量和行号一样
        print(str(j)+'*'+str(i)+'='+str(i*j), end='\t')
    print()

~~~

















