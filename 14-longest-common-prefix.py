#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
# 
# compare ASCII
#
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs : return ''
        smin = min(strs)
        smax = max(strs)
        for i in range(len(smin)):
            if smin[i] != smax[i]:
                return smin[:i]
        return smin

