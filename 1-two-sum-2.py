#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# 利用Python字典的哈希映射达到复杂度O(n)
# 牺牲空间复杂度 内存使用大于首尾递进查找

class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for index,num in enumerate(nums):
            a = target - num
            if a in dict.keys():
                return [dict[a],index]
            dict[num] = index
        return None

