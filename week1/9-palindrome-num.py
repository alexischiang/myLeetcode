#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
class Solution:
    def isPalindrome(self, x): 
        st = str(x)
        if st[::-1] == str(x):
            return True
        else:
            return False
        
        

