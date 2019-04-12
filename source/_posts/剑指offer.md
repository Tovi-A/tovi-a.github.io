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
# 合并两个排序的链表
题目链接：[题目链接](https://www.acwing.com/problem/content/34/)
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
    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode* dumy = new ListNode(0);
        ListNode* res = dumy;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                dumy->next = l1;    //尾插法
                l1 = l1->next;
            }
            else {
                dumy->next = l2;
                l2 = l2->next;
            }
            dumy = dumy->next;
        }
        if (l1)     dumy->next = l1;
        if (l2)     dumy->next = l2;
        return res->next;
    }  
};
```
# 树的子结构
题目链接：[题目链接](https://www.acwing.com/problem/content/35/)<br>
题解：[题解](https://www.acwing.com/solution/acwing/content/745/)
```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool hasSubtree(TreeNode* pRoot1, TreeNode* pRoot2) {
        if (!pRoot1 || !pRoot2)     return false;
        if (isSame(pRoot1, pRoot2))     return true;
        return hasSubtree(pRoot1->left, pRoot2) || hasSubtree(pRoot1->right, pRoot2);
    }
    
    bool isSame(TreeNode* pRoot1, TreeNode* pRoot2) {
        if (!pRoot2)    return true;
        if (!pRoot1 || pRoot1->val != pRoot2->val)  return false;
        return isSame(pRoot1->left, pRoot2->left) && isSame(pRoot1->right, pRoot2->right);
    }
};
```
# 二叉树的镜像
题目链接：[题目链接](https://www.acwing.com/problem/content/37/)<br>
题解：[题解](https://www.acwing.com/solution/acwing/content/746/)
```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void mirror(TreeNode* root) {
        if (root == NULL)   return ;
        swap(root->left, root->right);
        mirror(root->left);
        mirror(root->right);
    }
};
```
# 对称的二叉树
题目链接：[题目链接](https://www.acwing.com/problem/content/38/)<br>
题解：[题解](https://www.acwing.com/solution/acwing/content/747/)
```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return !root || dfs(root->left, root->right);
    }
    
    bool dfs(TreeNode *p, TreeNode *q) {
        if (!p || !q)   return !p && !q;
        return p->val == q->val && dfs(p->left, q->right) && dfs(p->right, q->left);
    }
};
```
# 顺时针打印矩阵
题目链接：[题目链接](https://www.acwing.com/problem/content/39/)<br>
题解：[题解](https://www.acwing.com/solution/acwing/content/748/)
```C++
class Solution {
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        vector <int> res;
        int n = matrix.size();
        if (!n)     return res;
        int m = matrix[0].size();
        
        vector<vector<bool>> st(n, vector<bool>(m, false));
        int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};   //四个方向，上右下左
        int x = 0, y = 0, d = 1;    //d表示方向，开始第一个下标
        
        for (int i = 0; i<n * m; i++) {
            res.push_back(matrix[x][y]);
            st[x][y] = true;
            int a = x + dx[d], b = y + dy[d];
            if (a < 0 || a >= n || b < 0 || b >= m || st[a][b]) {
                d = (d+1) % 4;
                a = x + dx[d], b = y + dy[d];
            }
            x = a, y = b;
        }
        return res;
    }
};
```
# 包含min函数的栈
题目链接：[题目链接](https://www.acwing.com/problem/content/90/)<br>
题解：[题解](https://www.acwing.com/solution/acwing/content/749/)
```C++
class MinStack {
public:
    /** initialize your data structure here. */
    stack <int> s;
    stack <int> Min;
    MinStack() {
        
    }
    
    void push(int x) {
        s.push(x);
        if (Min.empty() || Min.top() > x)   Min.push(x);
    }
    
    void pop() {
        if (s.top() == Min.top())   Min.pop();
        s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return Min.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```
# 栈的压入、弹出序列
题目链接：[题目链接](https://www.acwing.com/problem/content/40/)
```C++
class Solution {
public:
    bool isPopOrder(vector<int> pushV,vector<int> popV) {
        if (pushV.size() != popV.size())   return false;
        stack <int> s;
        int num = 0;
        for (int i = 0; i<pushV.size(); i++) {
            s.push(pushV[i]);
            while (!s.empty() && popV[num] == s.top()) {
                s.pop();
                num ++ ;
            }
        }
        if (s.empty())  return true;
        return false;
    }
};
```
# 不分行从上往下打印二叉树
题目链接：[题目链接](https://www.acwing.com/problem/content/41/)
```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> printFromTopToBottom(TreeNode* root) {
        vector <int> res(0);
        queue <TreeNode*> q;
        if (root == NULL)   return res;
        q.push(root);
        while (!q.empty()) {
            TreeNode* cur = q.front();
            q.pop();
            res.push_back(cur->val);
            if (cur->left)  q.push(cur->left);
            if (cur->right)     q.push(cur->right);
        }
        return res;
    }
};
```
# 分行从上往下打印二叉树
题目链接：[题目链接](https://www.acwing.com/problem/content/description/42/)<br>
```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> printFromTopToBottom(TreeNode* root) {
        vector<vector<int>> res;
        if (!root)  return res;
        
        queue<TreeNode* > q;
        q.push(root);
        q.push(nullptr);        //队列里面加一个标记nullptr表示这一层已经结束了
        
        vector<int> level;
        while (q.size()) {
            auto t = q.front();
            q.pop();
            if (!t) {
                if (level.empty())  break;
                res.push_back(level);
                level.clear();
                q.push(nullptr);
                continue;
            }
            level.push_back(t->val);
            if (t->left)    q.push(t->left);
            if (t->right)   q.push(t->right);
        }
        return res;
    }
};
```