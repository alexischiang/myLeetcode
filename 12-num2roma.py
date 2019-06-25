#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
# 
# ✔ Accepted
#   ✔ 3999/3999 cases passed (52 ms)
#   ✔ Your runtime beats 99.88 % of python3 submissions
#   ✔ Your memory usage beats 98.86 % of python3 submissions (13 MB)
# mySolution 穷举

class Solution:
    def intToRoman(self, num):
        mystr = ''
        a = num//1000
        mystr += ('M' * a)
        rem = num%1000
        while rem:
            if rem >= 100 and rem < 1000:
                if rem >= 900:
                    rem = rem%900
                    mystr += ('CM')
                elif rem >= 500 and rem < 900:
                    rem = rem%500
                    mystr += ('D')
                elif rem >= 400 and rem < 500:
                    rem = rem%400
                    mystr += ('CD')
                elif rem%100 == 0:
                    mystr += (rem//100)* 'C'
                    rem = 0
                else:
                    mystr += (rem//100)* 'C'
                    rem = rem%100
            elif rem >= 10 and rem < 100:
                if rem >= 90:
                    rem = rem%90
                    mystr += ('XC')
                elif rem >= 50 and rem < 90:
                    rem = rem%50
                    mystr += ('L')
                elif rem >= 40 and rem < 50:
                    rem = rem%40
                    mystr += ('XL')
                elif (rem%10 == 0):
                    mystr += (rem//10)*'X'
                    rem = 0
                else:
                    mystr += (rem//10)*'X'
                    rem = rem%10
            elif rem > 0  and rem < 10:
                if rem == 9:
                    mystr += ('IX')
                    rem = 0 
                elif rem >= 5 and rem < 9:
                    rem = rem%5
                    mystr += ('V')
                elif rem == 4:
                    mystr += ('IV')
                    rem = 0
                else:
                    mystr += (rem * 'I')
                    rem = 0
        return mystr    

