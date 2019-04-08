---
title: 剑指offer
date: 2019-04-08 20:48:08
tags:
- 剑指offer
categories: 算法
comments: true
mathjax: true
---
# 调整数组顺序使奇数位于偶数前面
题目链接：[题目链接](https://www.acwing.com/problem/content/30/)<br>
题解：[题解](https://www.acwing.com/solution/acwing/content/738/)
```C++
class Solution {
public:
    void reOrderArray(vector<int> &array) {
        int l = 0, r = array.size()-1;
        while (l < r) {
            while (array[l]%2 == 1)     l ++;
            while (array[r]%2 == 0)     r --;
            if (l < r)  swap(array[l], array[r]);
        }
    }
};
```
# 链表中倒数第k个节点
题目链接：[题目链接](https://www.acwing.com/problem/content/32/)<br>
题解：[题解](https://www.acwing.com/solution/acwing/content/740/)
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* findKthToTail(ListNode* pListHead, int k) {
        int n = 0;
        for (auto p = pListHead; p; p = p->next)    n ++ ;
        if (k > n)  return NULL;
        auto p = pListHead;
        for (int i = 0; i<n-k; i++)     p = p->next;
        return p;
    }
};
```
# 链表中环的入口结点
题目链接：[题目链接](https://www.acwing.com/problem/content/86/)<br>
题解：[题解](https://www.acwing.com/solution/acwing/content/741/)
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *entryNodeOfLoop(ListNode *head) {
        if (head == NULL || head->next == NULL)   return NULL;
        ListNode *first = head, *second = head;
        while (first && second) {
            first = first->next;
            second = second->next;
            if (second)     second = second->next;
            else    return NULL;
            
            if (first == second) {
                first = head;
                while (first != second) {
                    first = first->next;
                    second = second->next;
                }
                return first;
            }
        }
        return NULL;
    }
};
```
# 反转链表
题目链接：[题目链接](https://www.acwing.com/problem/content/33/)<br>
题解：[题解](https://www.acwing.com/solution/acwing/content/743/)
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *prev = NULL;
        ListNode *cur = head;
        while (cur) {
            ListNode *next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
};
```