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

