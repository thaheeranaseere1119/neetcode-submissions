# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while True:
            curr = prev
            for i in range(k):
                curr = curr.next
                if curr is None:
                    return dummy.next
            curr = prev.next
            before = curr
            prev_node = None
            for i in range(k):
                next_node = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = next_node
            prev.next = prev_node
            before.next = curr
            prev = before
        
        