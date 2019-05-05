---
title: leetcode
date: 2019-05-03 22:43:57
tags:
- leetcode
categories: 算法
comments: true
mathjax: true
---
# dfs-784. Letter Case Permutation
[题目链接](https://leetcode.com/problems/letter-case-permutation/)
```C++
class Solution {
public:
    vector<string> ans;
    
    vector<string> letterCasePermutation(string S) {
        dfs(S, 0);    
        return ans;
    }
    
    void dfs(string s, int u) {
        if (u == s.size()) {
            ans.push_back(s);
            return ;
        }
        dfs(s, u + 1);
        if (s[u] >= 'A') {
            s[u] ^= 32;
            dfs(s, u + 1);
        }
    }
};
```

```Python
class Solution:
    ans = []
    def dfs(self, s, u):
        s = list(s)
        if (u == len(s)):
            s = ''.join(s)
            self.ans.append(s)
            return 
        self.dfs(s, u + 1)
        if (s[u] >= 'A'):
            s[u] = chr(ord(s[u]) ^ 32) # ASCII码与字符相互转换
            self.dfs(s, u + 1)
    def letterCasePermutation(self, S: str) -> List[str]:
        self.ans = []
        self.dfs(S, 0)
        return self.ans
    
```



# dfs-77. Combinations

[题目链接](<https://leetcode.com/problems/combinations/>)

```C++
class Solution {
public:
    
    vector<vector<int>> ans;
    
    vector<vector<int>> combine(int n, int k) {
        vector<int> path;
        
        dfs(path, 1, n, k);
        
        return ans;
    }
    
    void dfs(vector<int> &path, int start, int n, int k) {
        if (k == 0) {
            ans.push_back(path);
            return ;
        }
        for (int i = start; i <= n; i ++) {
            path.push_back(i);
            dfs(path, i + 1, n, k - 1);
            path.pop_back();
        }
    }
};
```
```Python
class Solution:
    ans = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        self.ans = []
        self.dfs(path, 1, n, k)
        return self.ans
    
    def dfs(self, path, start, n, k):
        if k == 0:
            path = list(path)
            self.ans.append(path)
            return
        for i in range(start, n + 1):
            path.append(i)
            self.dfs(path, i + 1, n, k - 1)
            path.pop()
```
# dfs-257. Binary Tree Paths

[题目链接](https://leetcode.com/problems/binary-tree-paths/)

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
    
    vector<string> ans;
    
    vector<string> binaryTreePaths(TreeNode* root) {
        string path;
        dfs(root, path);
        
        return ans;
    }
    
    void dfs(TreeNode* root, string path) {
        if (!root)  return ;
        
        if (path.size())    path += "->";
        path += to_string(root->val);
        
        if (!root->left && !root->right)    ans.push_back(path);
        else {
            dfs(root->left, path);
            dfs(root->right, path);
        }
    }
};
```

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = []
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans = []
        path = ""
        self.dfs(root, path)
        return self.ans
    def dfs(self, root, path):
        if (not root):
            return 
        if (len(path)):
            path += "->"
        path = path + str(root.val)
        if (not root.left and not root.right):
            self.ans.append(path)
        else:
            self.dfs(root.left, path)
            self.dfs(root.right, path)
```

