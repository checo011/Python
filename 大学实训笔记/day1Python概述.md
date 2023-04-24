# Day1 Python概述

### 什么是Python

~~~markdown
Python是一门程序设计语言
1. 自然语言： 人听得懂的语言（汉语，英语，日语，法语，西班牙语）
2. 机器语言： 计算机能读懂的语言(C C++ Java JS PHP Python HTML SQL)
3. 程序设计语言： 自然语言和机器语言的桥梁（人和机器都能读懂）

语言的高级性：
1. 越接近于自然语言的编程语言越高级： Java Python   
2. 越接近于机器语言的编程语言越低级： 汇编    

越高级的语言，对人类越友好，但是执行效率越低
越低级的语言，对计算机越友好，执行效率越高

计算机能且只能读懂二进制
~~~

* Python的历史

~~~markdown
1. Python之父： Guido van Rossum  --龟叔
2. 龟叔喜欢一个马戏团Monty Python 
2. 诞生： 1989年圣诞节期间
~~~

* Python的特点

~~~markdown
主要特点：
1. 语法简洁且清晰优雅
2. 有强大的类库
3. 胶水语言
4. 纯面向对象的编程

其他特点：
1. 跨平台性---跨操作系统
2. 编译成字节码---虚拟机执行
3. 代码量较少（是Java代码量的5分之一）
~~~

* Python的运行机制

~~~markdown
源代码： 人写的代码
常见的运行机制：
1. 编译型：
		源代码---编译器---字节码文件（二进制文件，可执行文件）
		优势：一次编译，次次直接执行字节码---效率高
		劣势：不能跨平台
2. 解释型：
		源代码---解释器，直接翻译运行
		优势：可以跨平台
		劣势：每次都需要重新翻译---效率低
		
3. Python的运行机制：
		1. 脚本：解释型
		2. 先编译，后解释运行
		源代码---编译器---字节码文件---解释器（PVM，虚拟机中包含了解释器）
		
~~~

* Python 应用场景

~~~markdown
1. shell编程
2. 控制语言
3. 框架 
~~~

* Python的实现

~~~markdown
Python的虚拟机
1. CPython  
		原始的，标准的Python虚拟机（官方）
2. Jython
		Java实现的Python虚拟机
3. IronPython
		用.net架构实现的Python虚拟机
4. Psyco：
		Python的一个扩展模块，用与程序优化
5. Shed Skin：
		Python的一个编译器，将Python代码转换成c++
6. PyPy：
		Python实现的Python虚拟机
		动态编译机制--快		
~~~

### Python的安装

~~~markdown
1. 官网: www.python.org
2. Python 3.6x 
3. Python的默认安装路径：
		C：\\User\\用户名\\AppData\\local\\Programs\\Python\\Python36
~~~

* 检查

~~~markdown
cmd黑窗口： 键入  python  如果出现版本号：成功
如果出现 Python 不是内部或外部命令  没有配置环境变量


如果没有配置环境变量：
1. 我的电脑（此电脑，计算机）右键---点击属性  
2. 找到高级系统设置，并点击
3. 点击环境变量
4. 如果没有Path环境，则新建，如果有，直接在Path中添加
		添加Python安装路径即可
~~~



电脑：

处理器（开发）：  i5  i7  i3     

M: 4代---标压  5V       i5 - 4800M        i7-8300 U  

U:  低压CPU  1.2v-2.4v    内存： L DDR3  DD4

i7 8代   3000~5000 

H:  7000+ 

HQ:  高压     高超频 

HK：13000+   高端游戏本（可嵌入式）

F：i5-9400F   

钱：























