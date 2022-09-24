"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy, newDummy = Node(0), Node(0)
        dummy.next, newDummy.next = head, None
        curr, currNew = dummy, newDummy
        lut = {}
        
        while curr.next:
            currNew.next = Node(curr.next.val)
            curr, currNew = curr.next, currNew.next
            
            lut[curr] = currNew
            
        
        curr, currNew = dummy.next, newDummy.next
        while curr:
            
            lut[curr].random = lut[curr.random] if curr.random else None
            curr = curr.next
            
        return newDummy.next
        
        
        
        
        