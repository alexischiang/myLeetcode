#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# mySolution 列表
#

class Solution:
    def reverse(self, x):
        st = str(x)
        mylist = list(st)
        if mylist == ['0']:
            return int(mylist[0])
        elif len(mylist) == 1:
            return int(mylist[0])
        elif mylist[0] != '-':
            if mylist[0] != '0':
                mylist.reverse()
            elif mylist[0] == '0':
                mylist[1:].reverse()
        elif mylist[0] == '-':
            if mylist[1] != '0':
                templist = mylist[1:]
                templist.reverse()
                mylist = ['-'] + templist
            elif mylist[1] == '0':
                templist = mylist[2:]
                templist.reverse()
                mylist = ['-'] + templist
        if mylist[0] == '0':
            mylist = mylist[1:]
        result = int(''.join(mylist))
        if result >= -(pow(2,31)) and result <= (pow(2,31))-1:
            return result
        else:
            return 0
