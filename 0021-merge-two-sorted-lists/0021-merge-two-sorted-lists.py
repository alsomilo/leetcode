# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1,ptr2 = list1,list2
        
        while not ptr1 and not ptr2:

            val1 = ptr1.val
            val2 = ptr2.val
                
                
            if val1 >= val2:
                temp = ptr2.next
                ptr2.next = ptr1
                ptr2 = temp
            else:
                temp = ptr1.next
                ptr1.next = ptr2
                ptr1 = temp 
    '''
    
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                cur.next = l2
                tmp = l2.next
                l2.next = l1
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
            
                
                
        
        