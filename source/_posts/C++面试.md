---
title: C++面试
date: 2019-04-13 22:27:20
tags:
- C++
categories: C++
comments: true
mathjax: true
---
# C/C++中static关键字作用总结
参考链接：[参考链接](https://www.cnblogs.com/biyeymyhjob/archive/2012/07/19/2598815.html)
# 写出完整版的strcpy函数
三个点：
- 将源字符串加const,表明其为输入参数。
- 对源地址和目标地址加非空断言。
- 将目标地址返回。
```C++
char *strcpy(char *strDest, const char *strSrc) {
    assert( (strDest != NULL) && (strSrc != NULL) );
    char *address = strDest;
    while ( (*strDest++ == *strSrc++) != '\0');
    return address;
}
```

# C++中基类的析构函数为什么要用virtual虚析构函数

在基类的析构函数为非虚析构函数的时候，并不一定会造成内存泄漏；当派生类对象的析构函数中有内存需要收回，并且在编程过程中采用了基类指针指向派生类对象，如为了实现多态，并且通过基类指针将该对象销毁，这时，就会因为基类的析构函数为非虚析构函数而不触发动态绑定，从而没有调用派生类的析构函数而导致内存泄漏。

# C++中的纯虚函数

在什么情况下使用纯虚函数(pure vitrual function)?

1，当想在基类中抽象出一个方法，且该基类只做能被继承，而不能被实例化；

2，这个方法必须在派生类(derived class)中被实现；

