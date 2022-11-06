# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        '''
        def mergTwo(l1, l2):
            if None in (l1, l2):
                return l1 or l2
            
            curr = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    curr, l1 = curr.next, l1.next
                else:
                    curr.next = l2
                    curr, l2 = curr.next, l2.next
            
            curr.next = l1 or l2
            return dummy.next
                    
        
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        res = lists[0]
            
        for i in range(1, len(lists)):
            res = mergTwo(res, lists[i])
            
        return res
        '''
        def mergTwo(l1, l2):
            if None in (l1, l2):
                return l1 or l2
            
            curr = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    curr, l1 = curr.next, l1.next
                else:
                    curr.next = l2
                    curr, l2 = curr.next, l2.next
            
            curr.next = l1 or l2
            return dummy.next
           
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        if len(lists) == 2:
            return mergTwo(lists[0], lists[1])
        
        split = len(lists)//2
        
        return mergTwo(self.mergeKLists(lists[:split]), self.mergeKLists(lists[split:]))