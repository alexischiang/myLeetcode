#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# my solution
# 判断前两位后对应切片

class Solution:
    def reverse(self, x):
        a = str(x)
        if a[0] != '-' and a != '0':
            if a[0] != '0':
                result = int(a[::-1])
            elif a[0] == '0':
                result = int(a[1:][::-1])
        elif a[0] == '-':
            if a[1] != '0':
                result =  int('-' + a[1:][::-1])
            elif a[1] == '0':
                result =  int('-' + a[2:][::-1])
        elif a == '0':
            result =  int(a)
        if result >= -(pow(2,31)) and result <= (pow(2,31))-1:
            return result
        else:
            return 0
