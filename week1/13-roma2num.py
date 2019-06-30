#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
# !!!!
# 遍历经过 IVIV 的时候先记录 II 的对应值 11 再往前移动一步记录 IVIV 的值 33，
# 加起来正好是 IVIV 的真实值 44
# max 函数在这里是为了防止遍历第一个字符的时候出现 [-1:0][−1:0] 的情况

class Solution:
    def romanToInt(self, s):
        roma_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':3,
            'IX':8,
            'XL':30,
            'XC':80,
            'CD':300,
            'CM':800
        }
        # 遍历字符串时不需要强制转换为list
        # 可直接使用enumerate
        # 核心 dict.get(key, default=None)
        # 有两位则返回两位对应 无则返回一位
        return sum(roma_dict.get(s[max(i-1,0):i+1],roma_dict[n]) for i,n in enumerate(s))

