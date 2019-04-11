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