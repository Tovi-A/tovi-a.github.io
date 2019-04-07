---
title: C++知识点
date: 2019-03-23 07:46:24
tags:
- C++
categories: C++
comments: true
mathjax: true
---
# 什么是深复制？什么是浅复制？（深拷贝与浅拷贝）  
参考链接：[深拷贝与浅拷贝](https://blog.csdn.net/bluescorpio/article/details/4322682)  
所谓浅拷贝，指的是在对象复制时，只是对对象中的数据成员进行简单的赋值，上面的例子都是属于浅拷贝的情况，默认拷贝构造函数执行的也是浅拷贝。大多情况下“浅拷贝”已经能很好地工作了，但是一旦对象存在了动态成员，那么浅拷贝就会出问题了，让我们考虑如下一段代码：  
```C++
class Rect
{
public:
	Rect()		// 构造函数，p指向堆中分配的一空间
	{
		p = new int(100);
	}
	~Rect()		// 析构函数，释放动态分配的空间
	{
		if(p != NULL)	
		{
			delete p;
		}
	}
private:
	int width;
	int height;
	int *p;		// 一指针成员
};

int main()
{
	Rect rect1;
	Rect rect2(rect1);   // 复制对象
	return 0;
}
```
在这段代码运行结束之前，会出现一个运行错误。原因就在于在进行对象复制时，对于动态分配的内容没有进行正确的操作。
具体分析见链接。
在“深拷贝”的情况下，对于对象中动态成员，就不能仅仅简单地赋值了，而应该重新动态分配空间，如上面的例子就应该按照如下的方式进行处理：
```C++
class Rect
{
public:
	Rect()		// 构造函数，p指向堆中分配的一空间
	{
		p = new int(100);
	}
	Rect(const Rect& r)
	{
		width = r.width;
		height = r.height;
		p = new int;	// 为新对象重新动态分配空间
		*p = *(r.p);
	}
	~Rect()		// 析构函数，释放动态分配的空间
	{
		if(p != NULL)	
		{
			delete p;
		}
	}
private:
	int width;
	int height;
	int *p;		// 一指针成员
};
```