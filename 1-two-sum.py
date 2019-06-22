#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# 首尾递进查找方法
# O(nlogn)

class Solution:
    def twoSum(self, nums, target):
        # 索引排序
        sorted_id = sorted(range(len(nums)),key= lambda k:nums[k])
        head = 0
        tail = len(nums)-1
        sum = nums[sorted_id[head]] + nums[sorted_id[tail]]
        # 当和大于目标时 调选一个较小得数相加 反之
        while sum != target :
            if sum > target :
                tail -= 1
            elif sum < target :
                head += 1
            sum = nums[sorted_id[head]] + nums[sorted_id[tail]]
        return [sorted_id[head],sorted_id[tail]]

