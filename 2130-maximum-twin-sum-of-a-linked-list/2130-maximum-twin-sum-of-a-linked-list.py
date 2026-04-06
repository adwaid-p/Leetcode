# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr = slow
        
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        midHead = prev

        maxSum = 0
        while midHead:
            maxSum = max(maxSum, head.val + midHead.val)
            head = head.next
            midHead = midHead.next
        
        return maxSum
