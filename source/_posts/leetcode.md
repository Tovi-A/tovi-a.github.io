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

# dfs-93. Restore IP Addresses

[题目链接](<https://leetcode.com/problems/restore-ip-addresses/>)

```C++
class Solution {
public:
    
    vector<string> ans;
    
    vector<string> restoreIpAddresses(string s) {
        string path;
        dfs(s, 0, 0, path);
        return ans;
    }
    
    void dfs(string &s, int u, int k, string path) {
        if (u == s.size()) {
            if (k == 4) {
                ans.push_back(path.substr(1));
            }
            return ;
        }
        
        if (k > 4)  return ;
        
        if (s[u] == '0')    dfs(s, u + 1, k + 1, path + ".0");
        else {
            for (int i = u, t = 0; i < s.size(); i ++ ) {
                t = t * 10 + s[i] - '0';
                if ( t < 256)   dfs(s, i + 1, k + 1, path + '.' + to_string(t));
                else    break;
            }
        }
    }
};
```

# dfs-95. Unique Binary Search Trees II

[题目链接](https://leetcode.com/problems/unique-binary-search-trees-ii/)

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
    vector<TreeNode*> generateTrees(int n) {
        if (!n)     return vector<TreeNode*>();
        return dfs(1, n);
    }
    
    vector<TreeNode*> dfs(int l, int r) {
        vector<TreeNode*> res;
        if (l > r) {
            res.push_back(NULL);
            return res;
        }
        
        for (int i = l; i <= r; i ++ ) {
            auto left = dfs(l, i-1), right = dfs(i + 1, r);
            for (auto &lt : left) {
                for (auto & rt : right) {
                    auto root = new TreeNode(i);
                    root->left = lt, root->right = rt;
                    res.push_back(root);
                }
            }
        }
        return res;
    }
};
```

