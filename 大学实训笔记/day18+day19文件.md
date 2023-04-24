# 文件

* 什么是文件

~~~markdown
1. 常见的文件：
		.py  .exe .mp3 .mp4 .vsd .rmvb .avi .wav .ppt .xls  .doc  .docx 
2. 计算机中的文件：以计算机硬盘为载体的存储在计算机上的信息集合 
		aa.py   --- aa:文件名  .py 后缀    aa.py:文件本身
		后缀的作用：标明解析方式
		aa.pyd  ---  aa.dll 
~~~

* 打开文件

~~~markdown
1. open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
		file:文件的路径 ，相对路径/绝对路径
		mode：打开的方式
		encoding：编码方式   unicode:utf-8
2. open（）返回的是IO流对象
		IO对象，可以控制文件，获取文件的信息
~~~

* 文件打开的模式

~~~markdown
1. r: 只读
		文件可以读出来，但是不能写
2. w：只写
		文件可以写入，但不能读
		覆盖写，新的内容会覆盖掉旧的内容
3. a：追加写
		在原有的内容基础上，继续写其他内容
		
4. rb： 二进制只读
5. wb： 二进制只写
6. ab:  二进制追加写

普通操作：
		只能操作str类型的数据
二进制操作：
		能操作一切数据（一般情况下，不能直接操作str）
~~~

* 流的分类

~~~markdown
1. 字节流
		以字节为单位传输数据
		一个字节=8位  1位：一个二进制码  0 1  
		能传输一切文件
		一次只能传一个字节，效率低
		
2. 字符流
		以字符为单位传输数据
		只能传输字符串
		一次能传多个字节，效率高
		
		一个字符=看情况  2，3,4字节
~~~

* IO对象

~~~markdown
1. closed：
		判断IO流是否已经关闭
2. mode：
		返回当前的打开模式
3. name：
		返回文件的名称
4. close():
		关闭文件流，IO流
		文件的关闭是极其重要的：IO流在计算机中是一种珍贵的资源，使用完毕后，要及时关闭释放，目的：为了给别的程序留下IO空间
5. read([n=-1])
		按字符读取，不传入n，读出所有
		如果传入n（n大于0的整数）表示，要读取指定字符数
		read()会根据文件指针的位置，继续读取内容
		如果文件读取到了最后，再次使用read()不会返回任何内容
6. readline([limit=-1])
		按行读取
		limit不传：一次返回一行数据
		limit传入：按照本行的指定字符数读取数据
7. readlines([hint=-1])
		读取所有行的数据，并把每一行数据打包正列表的元素（包含换行符）
		hint：不传：一次返回所有行的数据
		hint：传入： 按照指定字节数返回数据，如果字节数超过或等于下一行数据，则将下一行整行返回
8. tell()
		返回文件指针的位置
		utf-8： 英文，普通符号： 1个字节
		        中文，转义字符：2个字节
9. seek(offset,whence):
		移动文件指针位置	
		offset:要移动的字节数
		whence:从某个位置移动到offset个字节的位置
			1:从当前位置
			2：从文件末尾位置
			0：从文件开头
		如果内容中包含多字节的单个内容（汉字，转义字符），注意文件指针要在内容元素的两边（不要让指针分割内容元素）
10. write(s)
		s：任何字符串
		如果s是str类型：需要使用普通操作
		如果s是二进制类型的数据：需要使用带有b的二进制操作
		将s写到指定文件中
11. writelines(lines):
		lines:一个列表，列表的元素可以是任何字符串
		以行的形式写出数据
		将列表中的每一元素，分别写到文件内容中
12. flush()
		清空缓存
		close()可以触发一次清空缓存
		缓存默认：4096或8192个字节
~~~

---

### 永久存储

~~~markdown
1. 序列化
		Python中的对象转换成二进制数据 称之为序列化
2. 模块：pickle
		dump(): 将数据进行序列化  对象-二进制
		load(): 反序列化         二进制-对象
~~~

~~~python
import pickle
# u=[
#     ['zhang3','123']
# ]
#
# f = open('user.feige',mode='wb')
# pickle.dump(u,f)  # 腌制  将对象制作到IO流对象中
# f.close()
def login():
    f = open('user.feige',mode='rb')
    u = pickle.load(f)
    f.close()

    name=input('请输入用户名：')
    pwd=input('请输入密码：')
    for i in u:
        if i[0]==name and i[1]==pwd:
            print('登录成功')
def regist():
    f = open('user.feige', mode='rb')
    u = pickle.load(f)
    f.close()

    name = input('请输入要注册的用户名：')
    pwd = input('请输入要注册的密码：')
    u.append([name,pwd])

    f = open('user.feige', mode='wb')
    pickle.dump(u,f)
    f.close()

# regist()
login()



# 字符串
# 二进制数据
# 源代码中的对象---序列化
~~~

* with- open 结构

~~~markdown
1. 语法：
		with open(file,mode,endcoding) as 变量：
			文件操作
2. 无需考虑资源关闭问题，Python会自动关闭
~~~

~~~python
with open('hehe.txt','r') as f:
    print(f.read())
~~~

---

