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

# 经典分类　　　
1. 不带指针的类(complex)
2. 带指针的类(string)
# 头文件中的防卫式声明　　　
```C++
#ifndef __COMPLEX__
#define __COMPLEX__

..........

#endif
```
# 模板(class template)
```C++
template<typename T>
class complex
{
public:
    complex (T r = 0, T i = 0) : re(r), im(i) {     }
    complex& operator += (const complex&);
    T real () const { return re; }
    T imag () const { return im; }
private:
    T re, im;

    friend complex& __doapl (complex*, const complex&);
}


{
    complex<double> c1(2.5, 1.5);
    complex<int> c2(2, 6);
}
```
# 内联函数(inline)
函数在类本体内定义则是内联函数，否则不是。所有函数都可以写成inline，但有些函数定义为inline，但是编译器没有能力将他做成inline。（函数过于复杂则不能）
# 访问级别　　　
private层变量只能class本体成员函数访问。
# 构造函数 
- 创建一个对象时候，一个函数会自动调用起来，这个函数就是构造函数。  
- 构造函数没有返回值。
- 构造函数可以有默认值。
- 初始化参数：仅构造函数才享有。　　　
> 构造函数有两个阶段：
1. 初始化阶段。（这就是初始化参数的效果，如果不那样做，就等于放弃了初始化阶段，从而效率变差。）
2. 赋值阶段。
```C++
class complex
{
public:
    complex (double r = 0, double i = 0) : re (r), im (i) { }   //初始化参数　
    /*
    相当于 complex (double r = 0, double i = 0) { re = r; im = i; }
    */
    complex& operator += (const complex&);
    double real () const { return re; }
    double imag () const { return im; }
private:
    double re, im;

    friend complex& __doapl (complex*, const complex&);
}

{
    complex c1(2, 1);
    complex c2;
    complex* p = new complex(4);
    ...
}
```
# 构造函数可以有很多个－overloading（重载）
```C++
    double real () const { return re; }
    void real (double r) { re = r; }
```

```C++
class complex
{
public:
    complex (double r = 0, double i = 0) : re (r), im (i) { }   //初始化参数　
    complex () : re(0), im(0) { }   //这种写法不行，会使得编译器犹豫不知道选择哪一个
    /*
    complex c1;
    complex c2();
    */
    complex& operator += (const complex&);
    double real () const { return re; }
    double imag () const { return im; }
private:
    double re, im;

    friend complex& __doapl (complex*, const complex&);
}
```