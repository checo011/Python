# 集合（set）

* 集合的创建

~~~markdown
1. 手工创建
		s = {1,2,3}
		{元素1，元素2，元素3...}
		注意： 没有手工创建的空集合
2. 构造方法
		set():  创建空集合---空集合：set()
		set(iterable):
				将可迭代对象的元素初始化为一个集合
~~~

* 集合的访问

~~~markdown
1. 访问所有元素
		遍历
~~~

* 集合的添加

~~~markdown
1. add(value):
		向集合中添加一个元素，如果该元素已经存在，则不会被添加
2. update(iterbale):
		将可迭代对象中的元素，更新到集合中
~~~

* 集合的删除

~~~markdown
1. clear()：
		清空集合
2. pop():
		随机删除一个元素，并返回
3. remove(value):
		从结合中删除某个元素
4. discard(value):
		从集合中删除一个数据，如果不存在则什么都不发生
~~~

* 集合的其他方法

~~~markdown
1. copy()
		浅拷贝
2. difference(s)
		与另一个集合求差集
		等价于： A-B
		返回新的结果
3. difference_update(s)
		与另一个集合求差集
		影响原集合
4. intersection(s)
		与另一个集合求交集
		等价于 A&B
5. intersection_update(s)
		与另一个集合求交集，修改原集合
6. isdisjoint(s)
		判断与另一个集合是否是分离集
7. issubset(s)
		判断是否是另一个集合的子集
8. issuperset(s)
		判断是否是另一个集合的父集
9. symmetric_difference(s)
		与另一个集合求对称差集
10. symmetric_difference_update(s)
		与另一个集合求对称差集，修改原集合
11. union(s)
		与另一个集合求并集
		等价于 A | B
~~~

* 集合的特点

~~~markdown
1. 字典的键 是由集合实现的
2. 集合的数据，没有顺序可言
3. 集合是无序的
4. 不支持索引操作
5. 不支持切片操作
6. 集合的元素是不可重复的
7. 集合是可迭代对象
~~~

---

