# 面向对象三大特性

### 封装

~~~markdown
1. 对象都有明确的边界，把属性保护在边界内部称之为封装
2. 封装---数据隐藏
3. 封装的粒度： 控制一个对象的范围
		粒度过大：导致对象过于复杂，不利于各司其职
		粒度过小：造成对象过于简单，让过程过于复杂
~~~

~~~python
class Mylist:  # list
    def __init__(self):
        self.l=[]

    def add(self,item):
        self.l.append(item)

    def get_all_item(self):
        return self.l

# 创建Mylist类型实例对象   Mylist---自定义的类
m = Mylist()
m.add(123)
m.add(456)

print(m.get_all_item())
~~~

### 继承

~~~markdown
动物类---狗类---猫类---鱼类
1. 父类，子类
		父类是子类共性的抽象
		父类有的，子类也有，
		子类有的，父类不一定有
2. 满足is a 的关系 
		子类 is a 父类

3. 父类： 超类，基类
		object：是所有类的父类---根类
4. 语法：
		class 子类(父类)：
		如果一个类没有声明父类，该类默认继承于object
		class A:   ---  class A(object):
~~~

* 继承的特点

~~~markdown
1. 子类可以继承父类的属性和方法
2. 子类不能继承父类的私有化属性和方法
3. Python中的继承是多继承
4. 向子类调用继承的方法，同名方法会根据继承顺序，逐个查找
5. 父类扩展了子类---继承的可扩展性
~~~

~~~python
class Father:
    __money=1000000
    def cost_money(self):
        print('林北 爱花钱')

class StepFather:  #干爹
    money=2000000

class Son(Father,StepFather):
    money = 1000

class Daughter(Son):
    pass

s = Son()
d = Daughter()
print(s.money)
print(d.money)
# print(s._Father__money)
# s.cost_money()
~~~

### 多态

~~~markdown

~~~

