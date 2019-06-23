#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
#  数学方法 数字半倒置
#  if x<0,x最后一位为0(x%10=0) 返回 false
#  当取出的数大于剩下的数时停止循环

class Solution:
    def isPalindrome(self, x):
        if x<0 or not x % 10 and x : return False
        part2 = 0
        while x > part2:
            x ,rem = x // 10, x % 10
            part2 = part2*10 + rem
        return x == part2 or x == part2//10
        
        
        

