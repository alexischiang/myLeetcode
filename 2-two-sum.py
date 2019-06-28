#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        result_list = ListNode(0)
        current_node = result_list
        carry = 0

        # l1 l2 都是node!!!
        while l1 or l2:

            # 将值取出 有则取值 无则取0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            s = x + y + carry
            carry = s//10
            current_node.next = ListNode(s%10) #注意追加节点不能仅赋值val 需要用class
            current_node = current_node.next

            # 如果当前为尾节点 (l1!=none and l1.next=none)
            # l1.next为空 下一次while将不会执行
            if (l1!=None) : l1 = l1.next
            if (l2!=None) : l2 = l2.next

        if (carry > 0): current_node.next = ListNode(1)
        return result_list.next


