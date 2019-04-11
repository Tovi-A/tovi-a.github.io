---
title: codeforces
date: 2019-04-10 22:23:54
tags: 
- codeforces
categories: 算法
comments: true
mathjax: true
---
# A. Ilya and a Colorful Walk
题目链接：[A. Ilya and a Colorful Walk](https://codeforces.com/contest/1119/problem/A)<br>
> 题目大意：有n个房子，每个房子染着不同的颜色，保证至少有两个房子有着不同的颜色，让你找出这n个房子中的两个不同颜色房子的最大距离是多少。

> 解法：分别固定首尾扫描n个房子。
```C++
#include <bits/stdc++.h>
using namespace std;

int a[300000+100];

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i<n; i++)   scanf("%d", &a[i]);
    int res = 0, l = 0, r = n-1;
    while (l < r && a[l] == a[r])   r--;
    res = r-l;
    l = 0, r = n-1;
    while (l < r && a[l] == a[r])   l++;
    if (r-l > res)  res = r-l;
    printf("%d\n", res);
    return 0;
}
```
# B. Alyona and a Narrow Fridge
题目链接：[B. Alyona and a Narrow Fridge](https://codeforces.com/contest/1119/problem/B)
> 题目大意：告诉你有n个瓶子与这n个瓶子的高度，冰箱的高度h，冰箱宽2，则让你求将前k个瓶子都能放入冰箱的最大值k。（瓶子必须放在架子之上）
> 解法：分别将前k个瓶子放入一个数组b，对b进行排序，从最高的开始，如果当前可以装，则取下下个，直到数组b中所有瓶子都能装下，则表示此k值可取。然后k增加1，循环~
```C++
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int a[1000+100];
int b[1000+100];

int main() {
    int n, h, res = 0; 
    scanf("%d%d", &n, &h);
    for (int i = 0; i<n; i++)   scanf("%d", &a[i]);
    for (int i = 0; i<n; i++) {
        int flag = 0, num = h;
        memset(b, 0, sizeof(b));
        for (int j = 0; j<=i; j++)  b[j] = a[j];
        sort(b, b+i+1);
        for (int j = i; j>=0; j--) {
            if (num >= b[j]) {
                num -= b[j];
                j --;
            }
            else {
                flag = 1;
                break;
            }
        }
        if (flag == 0)  res = i+1;  
    }
    printf("%d\n", res);
    return 0;
}
```