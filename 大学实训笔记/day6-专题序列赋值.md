# 专题：赋值

~~~markdown
a = b  把b中存储的首地址 赋值给了a
~~~

| 运算式                | 解释说明                   |
| --------------------- | -------------------------- |
| a='abc'               | 基本形式                   |
| a,b,c='A','B','C'     | 元组赋值                   |
| [a,b,c]=['A','B','C'] | 列表赋值                   |
| a,b,c=['A','B','C']   | 序列赋值                   |
| a,b,c=’ABC‘           | 序列赋值                   |
| a,*b='ABC'            | Python3之后才有   序列解包 |
| a=b=c='ABC'           | 多目标赋值                 |
| a+=1                  | 增强赋值                   |

* 序列赋值

~~~markdown
1. 等号左右的数据要一一对应
		不能过多，也不能过少

~~~

~~~python
a,b,c=1,2,3
print(a,b,c)

a,b,c='ABC'
print(a,b,c)

a,=10,
print(a)

# a,b,c=100  # 报错
# print(a,b,c)

# a,(b,c)='ABC'  # 报错
#
# print(a,b,c)


# s='ABCD'
# a,(b,c)=s[:2],s[2:]  # 'AB' 'CD'
# print(a,b,c)
#
# a,(b,c)=[1,[2,3]]
# print(a,b,c)


# a,b,c=range(3)
# print(a,b,c)
#
# d = range(3)
# print(d)

# z=zip([1,2,3],[4,5,6])  # zip,是个迭代器
# a,b,c=z
# print(a,b,c)
# (a,b),(c,d),(e,f)=z
# print(a,b,c,d,e,f)

# for a,b in z:  #
#     print(a,b)


# 序列分割问题
l = [1,2,3,4]
while l:
    a,l=l[0],l[1:]
    print(a,l)
~~~

* 序列解包

~~~markdown
1. 星号表示： 获取剩下的所有数据，带有星号的变量，优先级低（让别的变量先赋值）
		a,*b = 1,2,3
		a:1
		b:[2,3]
2. 带有星号的变量可以没有值
3. 一个序列解包中，最多只能有一个带有星号的变量
~~~

~~~python
# 序列打包
a,*b = 1,2,3
print(a,b)

*a,b=1,2,3
print(a,b)

a,*b,c=1,2,3,4
print(a,b,c)

a,*b,c=1,2
print(a,b,c)

# *a,*b,c=1,2,3  # 报错
# print(a,b,c)

a,*b='ABCD'
print(a,b)

a,*b=range(10)
print(a,b)

a,*b,b=1,2,3
print(a,b)

a,b,*b=1,2,3
print(a,b)

a,*b=10,
print(a,b)

# 序列解包

a,*b=1,2,3
print(*b)

l=[1,2,3]
print(*l)

# 序列分割问题

l = [1,2,3,4]
while l:
    a,*l=l
    print(a,l)

~~~

---

