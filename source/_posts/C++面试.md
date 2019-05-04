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

