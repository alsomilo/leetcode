# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        ptrA, ptrB = headA, headB
        
        while ptrA or ptrB:
            if ptrA == ptrB:
                return ptrA
            

            
            if not ptrA:
                #print(f'ptrA ends! move to headB')
                ptrA = headB
            if not ptrB:
                #print(f'ptrB ends! move to headA')
                ptrB = headA
                
            if ptrA == ptrB:
                return ptrA
            
            ptrA = ptrA.next
            ptrB = ptrB.next
        return None
        
        
            
        