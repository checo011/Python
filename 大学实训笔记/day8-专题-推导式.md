# 专题： 推导式

~~~markdown
推导式是一种编程范式
通过的解析的形式生成数据
~~~

* 列表推导式

~~~markdown
1. 语法：
		[元素 for 变量 in 可迭代对象 if 布尔表达式 ]
		1. 元素： 最终列表使用的多有元素/每个元素
		2. for循环 ：控制循环次数（决定列表的长度） 提供数据源
		3. if语句： 对每一次循环进行筛选（条件）
		4. 元素的位置：可以是元素，可以是函数的调用，还可以是表达式
2. 列表推导式中，if语句可以省略
3. 特点：
		1. 书写方便
		2. 执行效率高
		3. 代码优雅，可读性高
~~~

~~~python
# l = [2,4,6]

# l = [i for i in range(2,7) if i%2==0]  # 2,3,4,5,6
# print(l)
# l = [i for i in range(2,7,2)]  # 2,3,4,5,6
# print(l)


# s = 'abcdef'
# l = []
# for i in s:
#     if i in 'ace':
#         l.append(i)
# print(l)
#
# print([i for i in s if i in 'ace'])

#
# sums = 0
# for i in range(1,101):
#     sums+=i
# print(sums)
#
# print(sum([i for i in range(1,101)]))
# print(sum([i for i in range(1,100,2)]))

# for i in range(1,10):
#     [print('%s*%s=%s'%(j,i,j*i),end='\t') for j in range(1,i+1)]
#     print()

# l = [print('hehe') for i in range(3)]
# print(l)

# 爱因斯坦的难题
# step=35
# while (step+1)%30!=0:
#     step+=7
# print(step)
#
# print([step for step in range(35,200,7) if (step+1)%30==0][0])

l = [[1,2,3],[1,2,3],[1,2,3]]

print(l)
print([[1,2,3]]*3)
print([[j for j in range(1,4)] for i in range(3)])

~~~

* 字典推导式

~~~markdown
1. 语法：
		{键：值 for 变量 in 可迭代对象 if 布尔表达式 }
		1. 键值对： 最终列表使用的多有元素/每个元素
		2. for循环 ：控制循环次数（决定列表的长度） 提供数据源
		3. if语句： 对每一次循环进行筛选（条件）
~~~

* 集合推导式

~~~Markdown
1. 语法：
		{元素 for 变量 in 可迭代对象 if 布尔表达式 }
		1. 元素： 最终列表使用的多有元素/每个元素
		2. for循环 ：控制循环次数（决定列表的长度） 提供数据源
		3. if语句： 对每一次循环进行筛选（条件）
		4. 元素的位置：可以是元素，可以是函数的调用，还可以是表达式
~~~

~~~python
# d = {k:v for k,v in [(1,2),(3,4,),(5,6)]}
# print(d)

# d = {'one':1,'two':2,'three':3}
# print({v:k for k,v in d.items()})

s = {i for i in range(10) if i<0}
print(s)
~~~

* 生成器

~~~markdown
g = (i for i in range(10))

按需供应
~~~

---

