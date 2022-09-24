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
        
        
        # first pass, do two things: 1) link the next node for each new node in the newly copied linked list 
        #                            2) Establish a link between original non-empty node to the newly created node (copied node), such that any NON-EMPTY original node has a mapped new Node
        while curr.next:
            #1) link the next node for each new node in the newly copied linked list 
            currNew.next = Node(curr.next.val)
            # advance both curr and currNew ptr
            curr, currNew = curr.next, currNew.next
            
            #2) Establish a link between original non-empty node to the newly created node (copied node), such that any NON-EMPTY original node has a mapped new Node
            lut[curr] = currNew
            
        
        #reset both curr and currNew ptr to the heads
        curr, currNew = dummy.next, newDummy.next
        
        # second pass, do one thing: 1) connect the random ptr for each new node in the newly coplied linked list, using the lut created in the first pass above. 
        
        #loop through each original node
        while curr:
            
            # original node's corresponding new node is lut[curr]. populate its random pointer, to be original node's random ptr node's mapped node(in new list), if that random ptr node is non-EMPTY. If emptry (None node), then populate with None too.
            # This is because if original's node's random node can be None , where None node will not be in lut, since only non-EMPTY node was saved into LUT
            lut[curr].random = lut[curr.random] if curr.random else None
            curr = curr.next
            
        return newDummy.next
        
        
        
        
        