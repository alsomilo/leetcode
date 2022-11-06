# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        curr = dummy = ListNode(-1, head)
        offset  = k-1
        
        for _ in range(offset):
            curr = curr.next
        
        front = curr
        
        curr = end = dummy
        offset = k + 1
        
        for _ in range(offset):
            end = end.next
        
        while end:
            curr = curr.next
            end = end.next
            
        back = curr
        
        if front is back:
            return head


        front.next, back.next = back.next, front.next
        front.next.next, back.next.next = back.next.next, front.next.next
        return dummy.next
        