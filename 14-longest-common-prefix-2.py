#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
# 
# 水平两两比较 利用find()
#
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res



