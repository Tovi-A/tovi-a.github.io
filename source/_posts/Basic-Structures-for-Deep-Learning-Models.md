---
title: Basic Structures for Deep Learning Models
date: 2019-04-11 11:12:37
tags:
- 李宏毅
- 深度学习
categories: 机器学习&深度学习
comments: true
mathjax: true
---
![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/1.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/2.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/3.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/4.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/5.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/6.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/7.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/8.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/9.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/10.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/11.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/12.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/13.png)
> 不容易过拟合，比较好的处理sequence.

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/14.png)
> h'与h、b'与b的维度必须都一样。

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/15.png)
> 双向RNN,f3存在的目的就是将f1与f2的output合在一起。

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/16.png)
> 椎体RNN，好处是可以将sequence缩短。

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/17.png)
> 一个RNN的样子。其中y是从h'算出来的。（最简单的RNN)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/18.png)
$c^t$ 、$h^t$接其他的LSTM,LSTM的输入有两个vector,h是变化非常快的，而c变化较慢（记住以前的information）

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/19.png)
LSTM的架构，将$x^t$与$h^{t-1}$分别乘以不同的matrix.

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/20.png)
$c^{t-1}$的作用。

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/21.png)
将$z^i$与$z$相乘，维度相同，再相加，得到$c^t$.

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/22.png)
再次循环，反复使用。

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/23.png)
GRU不像LSTM有两个速度不一样的输入。出的箭头表示乘上了一个matrix，上面那个等式是$h{t-1}$,GRU的运算量比较小。

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/24.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/25.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/26.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/27.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/28.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/29.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/30.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/31.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/32.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/33.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/34.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/35.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/36.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/37.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/38.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/39.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/40.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/41.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/42.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/43.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/44.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/45.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/46.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/47.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/48.png)

![image](https://media.githubusercontent.com/media/Tovi-A/tovi-a.github.io/hexo/Additional_Resources/lihongyi-kejian/49.png)