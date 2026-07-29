# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pre = node
        curr = node.next
        node.val = node.next.val
        while curr.next:
            curr.val = curr.next.val
            pre = curr
            curr = curr.next
        pre.next = None