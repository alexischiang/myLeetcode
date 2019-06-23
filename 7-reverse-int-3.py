#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# mySolution string

class Solution:
    def reverse(self, x):
        st = str(x)
        if x >= (-pow(2,31)) and x < 0:
            st = st[1:]
            st = st[::-1].lstrip('0')
            if int(st) > pow(2,31)-1:
                return 0
            else:
                return int('-' + st)
        elif x == 0:
            return 0
        elif x <= (pow(2,31)-1) and x > 0:
            st = st[::-1].lstrip('0')
            if int(st) > pow(2,31)-1:
                return 0
            else:
                return int(st)
        else:
            return 0



