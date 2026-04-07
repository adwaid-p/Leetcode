# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        crntNode = head
        nextNode = None

        while crntNode:
            nextNode = crntNode.next
            crntNode.next = prevNode
            prevNode = crntNode
            crntNode = nextNode

        head = prevNode
        return head