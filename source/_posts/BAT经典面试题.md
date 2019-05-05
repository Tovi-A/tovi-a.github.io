---
title: BAT经典面试题
date: 2019-05-04 23:12:41
tags:
- 面试
categories: 综合
comments: true
mathjax: true
---

# 实现一个Memcpy函数

**memcpy函数**的功能是从源内存地址的起始位置开始拷贝若干个字节到目标内存地址中。

```C++
void *memcpy(void *dst, const void *src, size_t len)
{
	if(NULL == dst || NULL == src){
 		return NULL;
 	}
  
 	void *ret = dst;
  
 	if(dst <= src || (char *)dst >= (char *)src + len){
  		//没有内存重叠，从低地址开始复制
        while(len--){
            *(char *)dst = *(char *)src;
            dst = (char *)dst + 1;
            src = (char *)src + 1;
        }
    }
    else{
        //有内存重叠，从高地址开始复制
        src = (char *)src + len - 1;
        dst = (char *)dst + len - 1;
        while(len--){
            *(char *)dst = *(char *)src;
            dst = (char *)dst - 1;
    	    src = (char *)src - 1;
        }
     }
     return ret;
}
```

